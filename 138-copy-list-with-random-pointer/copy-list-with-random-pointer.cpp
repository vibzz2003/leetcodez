/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
private:
void insertattail(Node* &head, Node* &tail, int d){
    Node* newnode = new Node(d);
    if(head==NULL){
        head = newnode;
        tail = newnode;
        return;
    }else{
        tail->next = newnode;
        tail = newnode;
    }
}
public:
    Node* copyRandomList(Node* head) {
        //1. create a cloned list
        //2. clones node ko add karo in between original list (random p[ointer still intact)
        //3. raqndom pointer copy karne hai 
        // temp -> next -> random = temp -> random -> next;
        // 1 2  3  4  5  x   (original linked list)
        // | /| /| /| /| /            |              mapped in real time to decrease space complexity where the mapping was used as storing is now used to point = O(n) se O(1)
        // 1  2  3  4  5     (cloned linked list)

        //4. revert changes done in step 2
        //5. return clonelist ka head

        Node* temp = head;
        Node* cloneHead = NULL;
        Node* cloneTail = NULL;
        while(temp!=NULL){
            insertattail(cloneHead, cloneTail, temp->val);
            temp = temp->next;
        }//end of step 1

        Node* originalnode = head;
        Node* clonenode = cloneHead;

        while(originalnode!=NULL && clonenode!=NULL){
            Node* next = originalnode->next;
            originalnode->next = clonenode;
            originalnode= next;

            next = clonenode->next;
            clonenode->next = originalnode;
            clonenode = next;
        }//end of step 2

        temp = head;
        while(temp!=NULL){
           if(temp->next!=NULL){
               temp->next->random = temp->random ? temp->random->next : temp-> random;
           }
           temp = temp->next->next;
        }//end of step 3

        originalnode = head;
        clonenode = cloneHead;

        while(originalnode!=NULL && clonenode!=NULL){
            originalnode->next = clonenode->next;
            originalnode= originalnode->next;

            if(originalnode!=NULL){
                clonenode->next = originalnode->next;
            }
            clonenode = clonenode->next;
        }//end of step 4
        return cloneHead;
        //end of step 5
    }
};