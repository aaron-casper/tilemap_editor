int lvl0098[32][40] =
{
    { 6,6,6,6,6,6,6,6,1,1,1,6,6,6,6,6,1,1,1,6,6,6,1,1,6,6,6,6,6,6,48,48,48,48,48,6,6,6,6,6 },
    { 6,6,6,6,192,6,6,6,1,1,1,6,6,6,6,6,6,6,6,6,6,1,1,1,6,6,6,6,6,6,48,48,48,48,1,6,6,6,6,6 },
    { 6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1,6,6,6,6,48,48,48,48,48,48,1,6,6,192,6 },
    { 6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,48,48,48,48,48,48,6,6,192,192,192 },
    { 6,6,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,48,48,48,48,48,48,6,6,6,192,192 },
    { 48,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,6,48,48,48,48,48,48,48,6,6,192,192,192 },
    { 48,48,48,48,48,48,6,1,6,6,6,6,6,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,48,48,48,48,48,48,48,6,6,192,192,192 },
    { 48,48,48,48,48,48,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,48,48,48,48,48,6,6,6,6,6,6 },
    { 48,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,6,234,234,234,234,234,6,6,6,6,6,6,6,6,6,6,6,6 },
    { 48,48,48,48,48,48,6,6,6,192,192,192,6,6,6,6,6,6,192,192,192,192,192,6,234,6,6,6,6,6,6,6,6,6,6,6,1,6,6,192 },
    { 48,48,48,48,48,6,6,6,6,6,192,192,6,6,6,6,6,6,192,192,192,192,192,6,234,6,234,234,6,6,6,6,6,6,6,1,1,6,6,6 },
    { 48,48,6,48,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,6,6,234,6,234,6,192,6,6,6,234,6,234,6,6,6,6,6 },
    { 48,48,48,6,6,6,6,6,6,6,6,6,6,1,1,1,1,6,6,192,192,192,6,6,234,6,234,6,192,234,234,234,234,6,234,6,234,234,234,6 },
    { 48,48,48,6,6,6,6,6,192,6,6,6,6,1,1,1,1,6,6,6,6,6,6,6,234,6,234,6,192,6,6,6,234,6,6,6,6,6,234,6 },
    { 48,48,48,6,6,6,6,6,192,6,6,6,6,6,1,1,6,6,234,234,234,234,234,234,234,6,234,6,234,234,234,6,234,234,234,234,234,234,234,6 },
    { 48,48,6,6,6,192,192,192,192,6,6,6,6,6,6,6,6,6,234,6,6,6,234,6,6,6,234,6,234,6,6,6,234,6,6,6,6,6,234,6 },
    { 6,6,6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,6,234,234,234,6,234,6,234,234,234,6,234,234,234,234,234,6,234,6,234,6,234,6 },
    { 6,6,6,6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,6,6,234,6,6,6,234,6,6,6,234,6,6,6,6,6,234,6,234,6,234,6 },
    { 6,6,6,6,6,6,6,192,192,6,6,1,6,6,6,6,6,6,234,6,234,234,234,6,234,6,234,234,234,6,234,234,234,234,234,6,234,6,234,6 },
    { 6,6,6,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,234,6,6,6,234,6,234,6,234,6,6,6,234,6,6,6,6,6,234,6,6,6 },
    { 6,6,6,6,1,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,1,1,1,1,6,6,6,6,6,234,234,6,234,234,234,234,234,234,234,6 },
    { 6,6,6,6,6,6,6,6,6,6,6,6,1,1,1,1,6,6,6,6,1,1,1,1,6,6,6,6,6,6,6,6,234,6,6,6,234,6,6,6 },
    { 6,6,6,6,1,1,6,6,6,6,6,6,6,1,6,6,6,6,6,6,1,1,1,1,6,6,6,6,6,6,234,234,234,6,234,234,234,6,234,234 },
    { 6,6,6,6,1,1,1,6,6,6,6,192,6,6,6,6,6,6,6,6,6,6,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,192 },
    { 6,6,6,6,6,6,1,6,6,6,6,192,192,6,6,6,6,6,6,6,6,6,6,6,6,6,192,192,6,6,6,6,6,6,1,6,6,6,192,192 },
    { 192,192,6,6,6,6,6,6,6,6,192,192,6,6,6,6,6,6,6,6,6,192,6,6,192,192,192,192,6,6,6,6,6,6,1,1,6,6,6,6 },
    { 192,192,192,192,192,6,6,6,6,6,192,192,192,6,6,6,6,6,6,6,6,192,192,192,192,192,192,192,6,6,6,6,6,6,1,1,6,6,6,6 },
    { 6,192,192,192,192,192,6,6,6,6,192,192,192,192,6,6,6,6,6,6,6,6,6,6,192,192,192,192,192,6,6,6,6,1,1,1,1,6,6,6 },
    { 6,192,192,192,192,192,6,6,6,6,6,48,48,48,6,6,6,6,6,6,6,6,6,6,6,6,192,192,192,192,6,6,6,6,1,1,1,1,6,6 },
    { 6,6,192,192,192,6,192,192,6,6,48,48,48,48,48,6,6,6,6,6,6,6,6,6,6,6,192,192,192,192,6,6,6,6,6,1,1,1,6,6 },
    { 6,6,6,6,6,6,192,192,6,6,48,48,48,48,48,6,6,6,1,1,1,1,6,6,6,192,192,192,192,192,6,6,6,6,6,1,1,6,6,6 },
    { 6,6,1,1,1,6,6,6,6,6,48,48,48,48,6,6,6,1,1,1,1,1,6,6,6,6,6,192,192,192,6,192,6,6,6,6,6,6,6,6 },
};