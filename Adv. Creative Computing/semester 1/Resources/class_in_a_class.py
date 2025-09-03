class lander:
    def __init__(self):
        print("outer_init")
        self.testing = 2
    class top:
        def __init__(self):
            print("inter_init")
            self.testing = 1
        
        def test():
            print("test")
    
    class top:
        def __init__(self):
            print("inter_init")
            self.testing = 1
        
        def test():
            print("test")
