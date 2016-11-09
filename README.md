# archive-scripts
Scripts which power an archive with reflink revisions

These scripts are for an archive system which captures the current state of the
systems being backed up. These current state backups are then reference linked
into dated directories. This uses features of btrfs, which has one data source
for all linked data, and the changes for each branch are stored seperately.

This archive system also has a cleaner which deletes old backups. This frees
space on the archive system. Tests in an anonymous production system reveal
that this btrfs archive system running daily backups can use a lot of space
over a short period of time.

You just run all to do scripts with cron.
