

class AaveV1Formal:
    def __init__(self, Aave) -> None:
        # user principal borrow balance
        self.B_x = 500

    @property
    def L_t(self):
        # sum total amount in reserves.
        pass

    @property
    def B_s(self):
        # sum amount borrowed at stable rate
        pass

    @property
    def B_v(self):
        # sum amount borrowed at variable rate
        pass
    
    @property
    def B(self):
        return self.B_s + self.B_v
    
    @property
    def U(self):
        # Utilization rate
        if self.L_t == 0:
            return 0
        else:
            self.B / self.L_t
    
    @property
    def U_optimal(self):
        # Target U by the model
        pass
    
    @property
    def R_v0(self):
        # constant for B_t = 0
        pass

    @property
    def R_slope1(self):
        # constant representing scaling of the interest rate vs utilization
        # when slope is below U < U-optimal 
        pass

    @property
    def R_slope2(self):
        # constant representing scaling of the interest rate vs utilization
        # when slope is above U >= U-optimal 
        pass

    @property
    def R_V(self):
        if self.U <= self.U_optimal:
            return (
                self.R_v0 + self.U/self.U_optimal * self.R_slope1
            )
        else:
            return (
                self.R_v0 + self.R_slope1 + (self.U-self.U_optimal)/(1- self.U_optimal) * self.R_slope2
            )

    @property
    def R_s(self):
        # see section 4.2
        pass

    @property
    def M_r(self):
        #
        pass
    

    def R_average_stable_rate_borrow_rate(self, amount):
        if self.B_s - amount == 0:
            return 0
        raise Exception("Not handled")
        return (
            1
        )

    @property
    def R_O(self):
        # overall borrow rate of the reserve
        if self.B == 0:
            return 0
        R_SA = 0
        return (
            self.B_v * self.R_V + self.B_s * R_SA # (TODO: what is R_SA -> I think it's the previous value)
            /
            self.B
        )

    @property
    def R_l(self):
        return self.U * self.R_O

    @property
    def C_liquidity_index(self):
        return (
            (self.R_l * self.T_Year + 1)

        ) * self.C_liquidity_index
    
    @property
    def C_i_0(self):
        # 1 ray
        return 10 ** 27

    @property
    def I(self):
        return (
            self.T_Year  * self.R_l + 1
        ) # TODO : this should include C_0^t-1
    
    @property
    def B_t_vc(self):
        DELTA_T = 1 # todo what is this ? Since last call ? 
        PREV_BT_VC = 1 # Recursive
        return (
            (1 + self.R_V / self.T_Year) * DELTA_T \
             * PREV_BT_VC
        )

    @property
    def B_xc(self):
        VARIABLE = True
        PREV = 1
        if VARIABLE: 
            return (
                self.B_t_vc / self.B_t_vc * (1 + self.R_V / self.T_Year) * 
                PREV * 
                self.B_x
            )
        else:
            return (
                (1 + self.R_s / self.T_Year) * self.B_x
            )

    @property
    def T_Year(self):
        return (3600 * 24 * 365)

    def H_f(self):
        pass        

