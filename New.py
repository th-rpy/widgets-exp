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
