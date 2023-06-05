def get_batches_bundles(raw_signals, pkg):

    charges_fields = {f for f in raw_signals.dtype.names if 'charge_num' in f}

    lots_fields = {f for f in raw_signals.dtype.names if 'lot_id' in f}

    lots_charges = {(raw_signals[f_charge_num], raw_signals[f_lot_id]) for f_charge_num, f_lot_id in zip(charges_fields, lots_fields) if f'pkg{pkg}' in f_charge_num and f'pkg{pkg}' in f_lot_id}

    lots_charges_nb = set()

    for bt_bd in lots_charges:

        if bt_bd not in lots_charges_nb:

            lots_charges_nb.add(bt_bd)

    batches_bundles = {(int(bundle[0]), int(bundle[1])) for bundle in lots_charges_nb if bundle[0].is_integer() and bundle[1].is_integer()}

    return PkgInfo(charges_fields, lots_fields, batches_bundles)



import numpy as np
import copy
import datetime as dt
from functools import lru_cache

class InsufficientDataError(Exception):
    pass

@lru_cache(maxsize=None)
def extract_dates(pkg: str, batch_bundle_sigs: dict, kiln_end_pos: float, kiln_start_pos: float) -> tuple:
    positions = batch_bundle_sigs[pkg]['location']
    locations_sig = copy.deepcopy(positions)
    times = batch_bundle_sigs['date time']

    if len(positions) > 1:
        mean_pos = np.mean((locations_sig >= kiln_start_pos) & (locations_sig <= kiln_end_pos))
        if mean_pos >= 0.01:
            mask = np.logical_and(locations_sig >= kiln_start_pos, locations_sig <= kiln_end_pos + 10)
            locations_sig = locations_sig[mask]
            times = times[mask]
            
            if len(locations_sig) >= 1:
                start_pos = min(locations_sig, key=lambda pos: abs(pos - kiln_start_pos))
                end_pos = min(locations_sig, key=lambda pos: abs(pos - kiln_end_pos))
                
                start_index = find_index(locations_sig, start_pos)
                start_date = times[start_index].astype(dt.datetime) if abs(start_pos - kiln_start_pos) < 0.5 else times[0].astype(dt.datetime)
                
                end_index = find_index(locations_sig, end_pos, reverse=True)
                end_date = times[end_index].astype(dt.datetime) if abs(end_pos - kiln_end_pos) < 5.0 else times[-1].astype(dt.datetime)
                
                drying_done = abs(end_pos - kiln_end_pos) < 5.0
                return start_date, end_date, drying_done
            else:
                raise InsufficientDataError("Not enough data between kiln_start_pos and kiln_end_pos")
        else:
            raise InsufficientDataError("Not enough data between kiln_start_pos and kiln_end_pos")
    else:
        raise InsufficientDataError("Not enough available data")

def find_index(arr, value, reverse=False):
    indices = np.where(arr == value)[0]
    return indices[-1] if reverse else indices[0]

