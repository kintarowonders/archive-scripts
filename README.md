# archive-scripts
Scripts which power an archive with reflink revisions using btrfs.

This system powers a btrfs based revision backup archive. It uses reference
linking in the btrfs filesystem. This allows copies to be in directories where
initial changes are shared in physical space but each copy can be independently
updated. This allows a server to save much space doing incremental backups as
revisions to the same physical data.

The script handles backups of servers (do-backup.py). It is used on Gentoo in
production and uses rsync to do backups. In the configuration there is an
archive directory. Backups are made into the archive directory's subdirectory
"current." This is just an update of what has changed on the target system
compared to what already exists in current.

The archive system makes a dated folder in the archive directory. This has the
current directory copied with permissions, recursively, as a reference link.
This script should be run frequently as has a few configuration options, such
as how many days of backups to keep, and where to keep the archives.

To configure just set cron to run the do-backup, do-archive, do-cleaner in that
order. The script is only designed for these scripts to be ran once a day as
the daily archives use folder names based only on the current date and do not
include timestamps.
