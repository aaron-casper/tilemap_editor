int lvl0191[32][40] =
{
    {1,1,1,1,2,2,2,2,2,3,3,3,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,1,1,1,1,2,3,3,3,3},
    {1,1,1,1,2,2,2,2,2,3,3,3,3,3,2,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,1,1,1,1,1,2,3,3,3,3},
    {2,2,2,2,2,1,1,2,2,3,3,3,3,3,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1,1,2,3,3,3,3},
    {2,2,2,2,1,1,1,1,2,2,3,3,3,3,2,2,2,2,3,3,3,3,3,3,3,2,2,2,2,2,1,1,1,1,1,2,3,3,3,3},
    {2,2,2,2,1,1,1,1,2,2,3,3,3,3,2,2,2,2,3,3,3,3,3,3,3,2,2,2,2,2,1,1,1,1,2,2,3,3,3,3},
    {2,2,2,1,1,1,0,1,1,2,3,3,3,3,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,1,1,1,1,2,2,2,2,3,2,2},
    {2,2,2,1,1,1,0,1,1,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2},
    {2,2,2,2,1,1,1,1,2,2,2,3,3,3,2,2,2,2,2,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1},
    {2,2,2,2,2,1,1,2,2,2,2,3,3,3,3,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,1,1},
    {2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,2,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,1,1},
    {3,3,3,2,2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,3,3,3,2,2,2,2,2,1,1,1,1,2,2,2,2,1,1},
    {3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3,3,2,2,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2},
    {3,3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2},
    {3,3,3,3,2,2,2,2,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2},
    {3,3,3,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2},
    {3,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2},
    {3,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,1,1,2,2,2,2,2,1,1,1,2,2},
    {3,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,1,1,2,2,2,2,1,1,1,1,1,2},
    {2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,1,2,2,3,3,2,1,1,1,1,1,2},
    {2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,1,1,2},
    {2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,1,1,1,1,2,3,3,3,3,2,2,1,1,1,1,2},
    {2,1,1,1,1,1,2,2,2,2,3,3,3,3,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,1,1,1,2,2},
    {1,1,0,0,1,1,2,2,2,3,3,3,3,3,3,2,2,2,3,3,3,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,1,2,2},
    {1,0,0,0,0,1,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2},
    {1,0,0,0,1,1,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2},
    {1,0,0,1,2,2,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,3,3,3,3,3,3,3,2,2},
    {1,1,1,2,2,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,0,0,0,1,1,2,3,3,3,3,3,3,3,3,2},
    {2,2,2,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,1,1,2,2,3,3,3,3,3,3,3,3},
    {2,2,2,3,3,3,3,3,3,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,0,0,1,1,2,2,3,3,3,3,3,3,3,3},
    {2,2,2,2,3,3,3,3,2,2,3,3,3,3,3,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3},
    {1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,2,2,1,1,1,1,1,1,2,2,2,2,2,2,3,2,2,2,3,3,3,3,2,2},
    {1,0,0,0,1,1,2,2,2,2,3,3,3,3,3,3,2,2,2,1,1,1,1,1,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2},
};
