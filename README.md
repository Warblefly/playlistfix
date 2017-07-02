# playlistfix

Converts Foobar2000 to Mixxx playlist

If you export a Foobar2000 playlist in m3u8 format, and try to import it into Mixxx for DJ-ing purposes,
you will find that the import fails. This is because Foobar2000 doesn't put certain metadata into
its exported m3u8 playlist.

This short Python program fixes this problem. It takes one parameter only: the name of the m3u8 playlist
which needs fixing.
