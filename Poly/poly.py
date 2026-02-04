# Name 1:Hoang Minh Nguyen
# EID 1:Htn937

# Name 2:
# EID 2:
import sys
class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data attribute, this node class has both 
    a coefficient and an exponent attribute, which is used to represent each 
    term in a polynomial.
    """
    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        self.dummy = Node(None, None)

        #self.head = None
    

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        new_node=Node(coeff,exp)
        prev=self.dummy
        current=prev.next

        while current is not None and current.exp>new_node.exp:
            prev=current
            current=current.next
            
        if  current is not None and current.exp == new_node.exp: 
            sum_coeff=current.coeff+new_node.coeff
            if sum_coeff != 0:
                current.coeff+=new_node.coeff
            else:
                prev.next=current.next

        else:
            new_node.next=current
            prev.next=new_node
        
                

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        result=LinkedList()
        p_prev=p.dummy
        p_current=p_prev.next
        prev=self.dummy
        current=prev.next
        
        while current is not None and p_current is not None:
            if current.exp == p_current.exp:
                coeff_sum = current.coeff + p_current.coeff
                if coeff_sum != 0:
                    result.insert_term(coeff_sum, current.exp)
                current = current.next
                p_current = p_current.next
            elif current.exp > p_current.exp:
                result.insert_term(current.coeff, current.exp)
                current = current.next
            else:
                result.insert_term(p_current.coeff, p_current.exp)
                p_current = p_current.next
        
        while p_current is not None:
            result.insert_term(p_current.coeff,p_current.exp)
            p_current=p_current.next
    
        while current is not None:
            result.insert_term(current.coeff,current.exp)
            current=current.next
        return result
        

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result=LinkedList()
        p_prev=p.dummy
        p_current=p_prev.next
        prev=self.dummy
        current=prev.next
        while current is not None: 
            
            while p_current is not None:

                multi_coeff = current.coeff * p_current.coeff
                sum_exp = current.exp + p_current.exp
                result.insert_term(multi_coeff, sum_exp)
                p_current=p_current.next
              

            current=current.next
            p_current=p_prev.next
            
        return result

    # Return a string representation of the polynomial.

    def __str__ (self):
        nodes_str = []
        prev= self.dummy
        current=prev.next
        while current is not None:
            nodes_str.append(str(current))
            current = current.next
        output = " + ".join(nodes_str)
        return output

def main():
    # read data from stdin and create polynomial p
    p=LinkedList()

    p_list=[]
    for line in sys.stdin:
        line = line.strip()
        p_list.append(line)
    n=int(p_list[0])
    for s in range(1,n+1):
        a=p_list[s].split()
        if int(a[0])!=0:
            p.insert_term(int(a[0]),int(a[1]))

    
    # read data from stdin and create polynomial q
    q=LinkedList()
    m=int(p_list[n+2])
    for s in range(n+3,n+m+3):

        b=p_list[s].split()
        if int(b[0])!=0:
            q.insert_term(int(b[0]),int(b[1]))
    # get sum of p and q as a new linked list and print sum
    sum_pq=p.add(q)
    print(sum_pq)
    # get product of p and q as a new linked list and print product
    mult_pq=p.mult(q)
    print(mult_pq)



if __name__ == "__main__":
    main()