int lvl0040[32][40] =
{
    {1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,2,3,3,3,3,3,3,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,1},
    {1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,2,2,3,3,3,3,3,2,2,2,2,3,3,3,3,3,3,3,3,2,2,2,2,1},
    {1,0,1,1,1,1,2,2,2,3,3,3,3,3,3,3,2,2,3,3,3,3,3,2,2,2,2,3,3,3,3,3,3,3,3,3,3,2,2,2},
    {1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,2,2,2,3,3,3,3,3,2,2,2,2,2,3,3,3,3,3,3,3,3,3,2,2,2},
    {1,1,1,1,1,2,2,2,2,3,3,3,3,3,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,2,2},
    {2,2,1,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,1,1,1,2,2,3,3,3,3,2,2,2},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,1,1,0,0,1,1,2,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,1,1,0,0,0,0,1,1,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,3,3,3,3,3,3,2,2,2,1,1,0,0,0,0,0,1,2,2,2,2,2,1},
    {2,2,2,2,2,2,2,2,1,1,1,0,1,1,2,2,3,3,3,3,3,3,3,2,2,2,1,1,1,0,0,0,0,1,1,2,2,2,2,1},
    {3,2,2,2,2,2,2,2,1,1,0,0,1,1,2,2,3,3,3,3,3,2,2,2,1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2},
    {2,2,2,2,2,2,2,2,1,1,0,0,1,2,2,3,3,3,3,3,2,2,1,1,1,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2},
    {2,3,3,3,3,3,2,2,1,1,1,1,2,2,3,3,3,3,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2},
    {2,3,3,3,3,3,3,2,2,1,1,2,2,3,3,3,3,2,2,2,1,1,1,1,1,2,2,2,3,3,3,2,2,2,1,1,1,1,2,2},
    {2,3,3,3,3,3,3,2,2,2,2,2,2,3,3,3,2,2,2,1,1,1,1,1,1,2,2,2,3,3,3,3,2,2,1,1,1,1,1,2},
    {2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,2,1,1,1,1,1,2},
    {2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,2,1,1,1,1,2,2},
    {1,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,2,3,3,3,3,2,1,1,1,1,2,3},
    {1,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,2,2,3,3,3,2,1,1,1,1,2,3,3,3,2,2,1,1,2,2,3},
    {1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,1,0,0,1,2,2,3,3,2,2,2,2,2,2,3},
    {2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,3,3,3,3,3,2,1,0,0,1,1,2,2,2,2,2,2,2,2,3,3},
    {2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,3,3,3,3,3,3,2,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3},
    {3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3},
    {3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3},
    {3,3,3,3,3,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,3,3,3,3,3,3,3,3},
    {3,3,3,3,2,2,2,2,1,1,1,1,1,2,2,3,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,3,3,3,3,3,3,3},
    {3,3,3,3,2,2,1,1,2,1,1,1,1,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,3,3,3,3,3,3,2},
    {3,3,3,2,2,2,1,2,2,2,1,1,1,2,2,3,3,2,2,2,2,2,2,2,2,2,2,1,1,0,1,1,2,2,3,3,3,2,2,2},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,1,1,2,2,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2},
    {2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2},
};
