# Finite State Machines

This week we are going to learn and practice a method to make your hardware in a well organize way: finite state machines.

A Finite state machines (FSM) gives an abstract organization to your hardware. FMS consists of several states, where a given state is chosen in responds to external inputs. Outputs of the systems depends on which state it is and in the external inputs as well.

:zap::zap:From now on, We want you to do all your hardware design using this!! :speak_no_evil::speak_no_evil: (or at least try...)

# Example: Turnstile Finite State Machine :suspension_railway: (wikipedia example)

Turnstiles are very simple example that can be modeled using a finite state machine. Once user deposit a coin (or ticket) the turnstile should unlock its arms, allowing a single user to pass. After the user passes through, the arms must be locked again until next users deposit a new coin (ticket).

![turnstile](pics/giphy_turnstile.gif "turnstile")

There are basically two states: locked and unlocked. The inputs for the systems are: deposit a coin, push the turnstile arm. Based on these constrains we can develop the following state diagram:

![turnstile_state](pics/330px-Turnstile_state_machine_colored.svg.png "s")

|  Current State |   Input|  Next State |  Output |
|---|---|---|---|
|  Locked | coin  | Unlocked  | Unlocks the turnstile so that the customer can push through.  |
|  Locked |  push | Locked  |  None |
|  Unlocked | coin  | Unlocked  | None  |
| Unlocked |  push  |  Locked | When the customer has pushed through, locks the turnstile.  |
