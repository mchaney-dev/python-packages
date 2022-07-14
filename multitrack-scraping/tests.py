from mtscraping import mts

print('---DEBUG---')
print('\ncreating 1 mts object:')
mts = mts()
print('instance: ' + str(mts.instance))
print('total mts objects: ' + str(mts.instances))
print('\ncreating 1 track object:')
track = mts.track
print('track id: ' + str(track.track_id))
print('total track objects: ' + str(track.tracks))
print('creating 1 queue object:')
queue = track.queue
queue.add_item()
print('queue id: ' + str(queue.queue_id))
print('total queue objects: ' + str(queue.queues))
print('queue list: ' + str(queue.queue_list))
print('current queue item: ' + str(queue.current_item))
print('next queue item: ' + str(queue.next_item))