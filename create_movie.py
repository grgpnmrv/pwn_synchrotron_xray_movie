from tools import create_snapshots, create_movie


first_image = 100
last_image = 149


# Create snapshots of synthetic synchrotron
# x-ray emission of pulsar wind nebula model
create_snapshots(first_image, last_image)


# Create gif animation from snapshoths
create_movie(delay = 20)
