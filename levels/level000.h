int lvl0000[32][40] =
{
    { 1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1 },
    { 1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0 },
    { 0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1 },
    { 1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1 },
    { 0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0 },
    { 0,0,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1 },
    { 1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0 },
    { 1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1 },
    { 1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0 },
    { 1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0 },
    { 1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0 },
    { 1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1 },
    { 1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,1 },
    { 0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0 },
    { 0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0 },
    { 0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1 },
    { 1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1 },
    { 0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,1 },
    { 0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0 },
    { 0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1 },
    { 0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1 },
    { 0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1 },
    { 0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0 },
    { 0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0 },
    { 1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0 },
    { 0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0 },
    { 1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1 },
    { 1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0 },
    { 1,1,0,0,1,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0 },
    { 1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0 },
    { 0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0 },
    { 1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0 },
};