# archive-scripts
Scripts which power an archive with reflink revisions using btrfs.

This system powers a btrfs based revision backup archive. It uses the reference
linking feature in the btrfs filesystem. This allows copies to be in directories
where initial changes are shared in physical space but each copy can be indepen-
dently updated. This allows a server to save much space doing incremental backups
as revisions to the same physical data.

The archive script obtains the systems listed in the config file (config.py) as
rsync pulls of / as root on those systems. Its best to set up passwordless SSH
to your systems, which are ideally Gentoo GNU/Linux or Arch Linux systems. It
then creates a reference link to a location named after the current day.

Reference links in btrfs create a copy, using the same physical data as the or-
iginal. Changes to these two filesystem locations however are stored in sepera-
te physical parts of the disks. So each daily backup creates a revision effici-
ntly linked to the master.

# Configuring and restoring

You must use btrfs as it has the reflink functionality for the filesystem in
the archivePath variable, usually /archive.

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
