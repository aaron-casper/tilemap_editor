int lvl0008[32][40] =
{
    { 192,6,6,6,6,6,6,6,6,6,6,1,1,6,234,234,234,234,234,234,234,6,234,234,234,6,234,6,234,234,234,234,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,6,6,6,6,6,1,1,1,6,6,6,6,6,234,6,6,6,234,6,6,6,6,6,234,6,6,6,6,6,6,6,6,6,6,6 },
    { 192,6,6,6,6,6,6,6,6,6,1,1,6,6,234,6,234,6,234,6,234,234,234,6,234,234,234,234,234,6,234,234,6,6,6,6,6,6,6,6 },
    { 6,192,6,6,6,6,1,6,6,1,6,1,1,1,234,6,234,6,6,6,6,6,234,6,234,6,6,6,234,6,234,6,6,6,6,6,192,192,6,6 },
    { 6,6,6,6,6,6,6,6,6,6,6,1,1,1,234,6,234,234,234,234,234,234,234,6,234,6,234,6,234,6,234,6,6,6,6,192,192,192,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,6,6,234,6,234,6,6,6,6,6,6,6,234,6,234,6,6,6,234,6,234,6,6,6,6,192,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,234,234,234,6,234,234,234,6,234,6,234,234,234,234,234,6,234,234,234,234,234,234,234,6,234,234,234,6,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,6,6,6,6,234,6,234,6,234,6,6,6,234,6,6,6,6,6,6,6,6,6,234,6,6,6,6,6 },
    { 6,6,6,192,6,6,234,6,234,6,234,234,234,234,234,6,234,6,234,234,234,6,234,6,234,234,234,234,234,234,234,234,234,234,234,234,234,6,6,192 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,6,6,234,6,234,6,234,6,6,6,234,6,6,6,234,6,6,6,234,6,6,6,6,6,234,6,6,192 },
    { 6,6,6,192,6,6,234,6,234,6,234,6,234,234,234,6,234,6,234,6,234,234,234,234,234,6,234,6,234,6,234,234,234,234,234,6,234,6,6,6 },
    { 6,6,6,192,192,6,234,6,6,6,234,6,6,6,6,6,234,6,6,6,6,6,6,6,234,6,234,6,234,6,6,6,6,6,234,6,234,6,6,6 },
    { 6,6,6,6,192,234,234,6,234,234,234,234,234,234,234,234,234,234,234,234,234,234,234,234,234,6,234,6,234,234,234,234,234,6,234,6,234,6,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,6,6,234,6,6,6,6,6,6,6,234,6,6,6,234,6,234,6,234,6,6,6,234,6,234,6,6,6,6,1 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,234,6,234,234,234,234,234,6,234,6,234,6,234,6,234,6,234,6,234,6,234,6,234,234,234,6,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,234,6,234,6,6,6,234,6,6,6,234,6,6,6,234,6,234,6,234,6,234,6,234,6,6,6,6,6 },
    { 6,6,6,6,6,6,234,6,234,6,234,6,234,6,234,6,234,234,234,6,234,234,234,234,234,6,234,6,234,6,234,6,234,6,234,6,234,6,192,192 },
    { 6,6,1,1,1,1,6,6,6,1,1,6,6,6,234,6,6,6,6,6,234,6,6,6,6,6,234,6,6,6,234,6,234,6,6,6,6,48,48,48 },
    { 6,6,6,1,1,1,6,6,6,1,6,1,6,6,234,6,234,234,234,234,234,6,234,234,234,234,234,234,234,234,234,6,234,234,1,1,48,48,48,48 },
    { 6,6,6,6,6,6,6,6,6,1,1,1,6,6,234,6,234,6,6,6,234,6,6,6,6,6,6,6,6,6,234,6,6,6,1,1,1,48,48,48 },
    { 6,6,6,6,6,6,6,6,6,6,6,1,6,1,234,6,234,6,234,6,234,234,234,234,234,234,234,6,234,6,234,234,234,234,6,6,1,48,48,48 },
    { 6,6,6,6,192,6,6,6,6,6,6,1,1,1,234,6,234,6,234,6,6,6,234,6,6,6,234,6,234,6,6,6,6,6,6,6,48,48,48,48 },
    { 6,6,6,6,192,192,192,192,6,6,6,1,1,1,234,234,234,6,234,6,234,6,234,6,234,6,234,234,234,234,234,234,234,234,6,48,48,48,48,48 },
    { 6,6,6,192,192,192,192,192,192,6,6,1,1,1,6,6,6,6,234,6,234,6,234,6,234,6,6,6,6,6,6,6,6,6,6,48,48,48,48,48 },
    { 6,6,6,6,6,192,192,192,6,6,6,1,1,1,234,234,234,234,234,6,234,6,234,6,234,234,234,234,234,234,234,234,234,6,6,6,48,48,6,6 },
    { 1,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,6,234,6,234,6,234,6,234,6,234,6,6,6,234,6,6,6,6,6,6,6,192,6 },
    { 1,1,1,1,6,6,6,6,6,6,6,6,6,6,234,234,234,6,234,234,234,6,234,6,234,6,234,6,234,6,234,6,234,234,6,6,6,192,192,6 },
    { 1,1,1,1,1,6,6,6,6,6,6,6,6,6,234,6,6,6,6,6,6,6,234,6,6,6,234,6,234,6,234,6,6,6,6,6,192,192,192,6 },
    { 1,1,1,1,1,6,6,6,6,6,6,6,6,6,234,234,234,234,234,234,234,234,234,234,234,6,234,234,234,6,234,6,234,6,6,6,192,192,192,6 },
    { 1,1,1,1,1,6,6,6,6,6,6,6,192,6,192,192,192,192,192,192,192,192,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,192,6,6 },
    { 6,6,1,1,1,6,6,6,6,6,192,192,192,192,192,192,192,192,192,192,192,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 1,6,6,1,6,6,6,6,6,6,192,192,192,192,192,192,6,192,192,192,192,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,192,6,6,6 },
};