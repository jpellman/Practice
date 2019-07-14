#!/usr/bin/env python
'''
Description:
Hacky little script to populate the file comment field on a Gzip file.

References:
https://tools.ietf.org/html/rfc1952#section-2.3.1.1
https://github.com/icsharpcode/SharpZipLib/blob/master/docs/specification/format.txt#L72-L95
https://www.forensicswiki.org/wiki/Gzip
'''

import sys

if len(sys.argv) != 2:
	sys.exit(1)

FNAME = sys.argv[1]
OUTPUT = "fcomment_" + FNAME
XLEN = 0
addition = b"Testing 1 2 3"

with open(FNAME, 'rb') as f:
	# Reads in the header (first 10 bytes)
	header = bytearray(f.read(10))
	with open(OUTPUT, 'wb') as g:
		# if FLG.FCOMMENT is not set
		# Set the flag on the new file, and then unset the
		# flag so the ensuing conditional that checks
		# this bit doesn't get messed up
		if not header[3] & 16:
			header[3] = header[3] + 16
			g.write(header)
			header[3] = header[3] - 16
		else:
			g.write(header)
		# if FLG.FEXTRA set
		if header[3] & 4:
			XLEN = f.read(2)
			g.write(f.read(XLEN))
		# if FLG.FNAME set
		if header[3] & 8:
			has_next_byte = True
			while has_next_byte:
				current_byte = f.read(1)
				has_next_byte= list(current_byte)[0]
				g.write(current_byte)
		# if FLG.FCOMMENT is not set
		if not header[3] & 16:
			g.write(addition)
			g.write(b"\x00")
		else:
			has_next_byte = True
			while has_next_byte:
				current_byte = f.read(1)
				has_next_byte= list(current_byte)[0]
				if not has_next_byte:
					g.write(addition)
				g.write(current_byte)
		# if FLG.FHCRC set
		# Does this logic really matter if we're not changing this?
		if header[3] & 2:
			g.write(f.read(2))
		# Dump all the rest of the compressed data
		g.write(f.read())

				
	


