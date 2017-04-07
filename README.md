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

# Configuring and restoring

You must use btrfs as it has the reflink functionality.

There are configuration options for what directories to exclude from rsync and
what servers to make backups of. This script is made for Gentoo systems and it
does Stage 4 rsync backups. List the servers to obtain and the directories you
wish to exclude, these should be the same as my defaults.

When restoring a backup you can just rsync the archive folders to your Gentoo
system and create the excluded directories, and reinstall the kernel and the
bootloader. After that you should be able to boot on similar hardware, if not I
am sure you know what you are doing.

# Cleaner

The cleaning script deletes archives more a certain age. The config.py sets
this age and the do-cleaner.py script deletes things older than that. Keep
in mind that because of the use of btrfs you can generally have it keep a
lot of revisions.

# Coming soon

I might add support so instead of archiveForDays it just has archiveRevisions
and that says how many revisions to archive. With this improvment there will be
a variable for the duration of revisions. This will allow snapshots to exist in
a much shorter timeframe.
