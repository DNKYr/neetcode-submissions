/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* ret = head;
        int total_len = 0;
        while (head != nullptr){
            total_len++;
            head = head->next;
        }
        head = ret;
        int pos_from_front = total_len - n;
        if (pos_from_front == 0){
            ret = ret->next;
            delete head;
            return ret;
        }
        for (int i = 0; i < pos_from_front - 1;++i){
            head = head->next;
        }
        ListNode* delete_node = head->next;
        head->next = head->next->next;
        delete delete_node;
        return ret;
    }
};
