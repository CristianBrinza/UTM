public final class Security extends Root implements SecurityInterface {

    public Security ( ) {
        objectsCount += 1;
        this.id = generateId ( );
    }

    @Override
    public boolean arrestRobber ( ) {
        // Chances to arrest a robber are equal to 80%
        int arrested = (int) ((Math.random ( ) * (99 - 1)) + 1);
        System.out.println (" ");
        if (arrested < 55) {
            System.out.println ("The security car with id   [" + this.id + "]   arrested the robber");
            return true;
        } else {
            System.out.println ("The security didn't manage to arrest the robber");
            System.out.println ("The robber stole all the money from the cash register");
            return false;
        }
    }

}
