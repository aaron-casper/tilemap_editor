int lvl0065[32][40] =
{
    { 6,1,1,1,1,6,6,192,192,192,6,6,6,6,6,6,6,6,1,6,6,1,1,6,6,192,192,6,6,6,6,6,6,192,192,6,6,6,6,6 },
    { 6,6,1,1,1,48,48,192,192,192,192,192,192,192,6,6,6,6,1,1,1,1,1,6,6,6,6,6,6,6,6,6,6,192,6,192,192,192,192,192 },
    { 192,192,6,6,48,48,48,48,48,192,192,192,192,192,192,6,6,1,1,1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,192,192,192,192,6,6 },
    { 192,6,6,48,48,48,48,48,48,48,192,192,192,192,192,192,6,6,1,6,6,1,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,192,6 },
    { 192,192,48,48,48,48,48,48,48,48,48,192,6,192,6,192,6,6,6,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,6 },
    { 6,6,48,48,48,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,48,48,48,48,48,48,48,48,48,6,6,6,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,48,48,48,48,48,48,48,48,48,6,6,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192 },
    { 192,48,48,48,48,48,48,48,48,48,6,48,48,48,48,48,48,48,48,6,192,192,6,6,6,6,1,6,6,6,192,6,6,6,6,6,6,6,6,6 },
    { 6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,192,6,6,6,6,1,1,6,6,192,192,192,6,6,6,6,6,6,6,6 },
    { 6,6,6,48,48,48,48,48,48,48,6,48,48,48,48,48,48,48,48,48,48,6,6,6,6,1,6,6,6,6,192,192,192,6,192,6,6,6,6,6 },
    { 1,6,6,6,6,48,48,48,48,6,48,48,48,48,48,48,48,48,48,48,48,1,1,1,6,6,6,6,6,6,6,192,192,192,192,6,6,6,6,6 },
    { 1,6,6,6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,1,1,6,6,6,6,6,6,6,192,192,192,6,6,6,6,6,6 },
    { 1,1,6,6,192,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,1,6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,6 },
    { 1,6,6,6,6,6,6,6,192,6,48,48,48,48,48,48,48,48,48,48,48,48,48,1,6,6,6,192,192,6,6,6,6,6,6,192,192,6,6,6 },
    { 6,6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,6,6,6 },
    { 6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,66,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,67,6,6,6,132,6,192,6,6,6,6,6,6,6 },
    { 1,6,6,6,6,6,6,48,48,48,48,48,48,48,48,6,48,48,48,48,48,1,6,6,6,6,130,6,6,6,6,6,6,6,6,6,6,1,6,1 },
    { 1,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,6,6,1,1,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,6,6,1,1,1,6,6,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,48,6,6,6,6,6,1,1,1,1,1,6,6,6,6,6,6,6,6,1 },
    { 6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,48,48,48,48,48,6,192,6,6,6,6,6,1,1,1,1,6,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,1,1,6,6,48,48,48,48,48,48,48,48,48,48,6,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,6,1,1,1,1,1,6,6,192,48,48,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,6,6 },
    { 6,6,6,1,1,1,1,6,192,192,192,192,192,48,6,6,6,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,6,6,6,192,192,6,6 },
    { 6,6,6,6,1,1,1,6,6,6,6,6,6,6,6,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,192,192,6,192,192,6,6 },
    { 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,6,6,192,6,6,6 },
    { 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192 },
    { 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,132,6,6,6,192,192,192,192,6,6,6,6,6,1,6,6,6,6,6,6,6,6,6,192,192 },
    { 6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,6,6,6,192,192,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 6,6,6,6,6,6,6,6,1,1,6,6,6,6,6,6,6,6,6,192,192,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6 },
};