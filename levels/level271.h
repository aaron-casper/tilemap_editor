int lvl0271[32][40] =
{
    {1,1,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2},
    {1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2},
    {1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,2,1},
    {1,1,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,2,1},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2},
    {2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,3,2,2},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,3,3,3,3,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,3,3,3,3,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,3,3,3,3,2,2,2,2,2,3,3},
    {2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3,2,2,2,2,2,3,2,2,2,2,2,2,3,3,3},
    {2,2,2,2,3,3,2,2,1,1,0,1,1,1,2,2,3,3,3,3,3,3,2,2,2,2,1,1,2,2,2,2,2,2,2,2,3,3,3,3},
    {3,3,3,3,3,3,2,2,1,1,0,1,1,1,2,2,2,3,3,3,3,2,2,2,2,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3},
    {3,3,3,3,3,3,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2},
    {2,3,3,2,2,3,3,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2},
    {2,2,2,2,3,3,3,3,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2},
    {2,2,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2},
    {2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2},
    {2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,1,1,1,1,2,2,3,3,2,2,1,1,1,2,2,2},
    {1,2,2,2,3,3,2,2,1,2,2,2,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,2,3,3,3,2,1,1,2,2,2,2},
    {1,2,2,2,3,3,2,1,1,1,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,1,1,2,3,3,3,2,2,1,2,2,2,2},
    {2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2},
    {2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,3,3,2,2,2,2,2,3,3,3,2,2,2,2,2,2,3,2},
    {2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,1,2,2,2,2,2,3,2,2,2,2,2,3,3,3,2,2,2,2,2,3,3,3,3},
    {3,3,3,2,2,2,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,3,3,3,3,3},
    {3,3,3,2,2,1,1,1,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,2,2,2,2,3,3,3,3,3},
    {3,3,2,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,3,3,3,3},
    {2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3},
    {2,2,2,1,1,1,1,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3},
    {2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,3,3,3},
    {2,2,2,2,2,2,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,3,3},
    {3,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2},
    {3,3,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2},
};
