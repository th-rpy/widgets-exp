
positions_sigs = [sig for sig in time_raw_signals.dtype.names if 'location' in sig]

positions_sigs_array = np.array(positions_sigs)  # Convert positions_sigs to a NumPy array

params, notif_ids, pkg_nbs, track_nbs = track_based_alerts_params(alerts_to_compute, positions_sigs_array)
dry_dev_min = params.get('dry_dev_min')
push_rate_max = params.get('push_rate_max')
min_time_on = params.get('min_time_on').astype(int)

mask = (100 <= time_raw_signals[positions_sigs_array]) & (time_raw_signals[positions_sigs_array] <= 290)

push_rate_avg = compute_push_rate_avg(position=time_raw_signals[positions_sigs_array][:, mask], times=time_raw_signals['date_time'][mask])
tdb_var = compute_tdb_var(time_raw_signals[mask], track_nbs, pkg_nbs)
spans = np.where((push_rate_avg < push_rate_max) & (tdb_var > dry_dev_min))[0]

Alerts = define_alerts_start_end(time_raw_signals['date_time'][mask], spans, min_time_on)
alert_notifs.update({notif_ids: Alerts})
