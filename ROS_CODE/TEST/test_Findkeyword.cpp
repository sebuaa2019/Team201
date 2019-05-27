#include<iostream>
#include<string>

int nSize = 5;
string arKeyword[] = {"hello","lease give me"," love you","obot is so dumb","anana"};

string FindKeyword(string inSentence)
{
    string res = "";
    int nSize = arKeyword.size();
    for(int i=0;i<nSize;i++)
    {
        int nFindIndex = inSentence.find(arKeyword[i]);
        if(nFindIndex >= 0)
        {
            res = arKeyword[i];
            break;
        }
    }
    return res;
}

int main(){
	assert(FindKeyword("print hello").compare("hello") == 0);
	assert(FindKeyword("Hello").compare("hello") == 0);
	assert(FindKeyword("Please give me a bottle").compare("lease give me") == 0);
	assert(FindKeyword("anana").compare("anana") == 0);
	return 0;
}
