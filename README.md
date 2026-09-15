# Software-Architecture-Weekly

## Development Notes

Before changing the program, the country-duration feature was placed in the
existing data-processing loop because that is where each record's duration is
already converted to hours. The JSON loading and duration conversion are
reused. The plot's record collection, sorting, labels, output file, and
display are left unchanged.

The country total includes matching records with a duration even when they do
not have a date. The plot still excludes those records because it needs a date
for the x-axis. This separation prevents the new calculation from omitting
valid EVA time while preserving the original plot behaviour.
