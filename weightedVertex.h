#include "tupleVertexWeight.h"

class weightedVertex{
    private tupleVW neighb[];
    private int key;
    public int getWeight(weightedVertex v)
    {
        for (int i = 0; i < this.neighb.Length; i++)
        {
            if(this.neighb[i].getV() == v)
                return this.neighb[i].getWeight();
        }
    }

}