package pe;

import java.util.*;

public class PE191
{
  private static enum WinningStates
  {
    ENDS_WITH_A_NO_L,
    ENDS_WITH_AA_NO_L,
    ENDS_A_HAS_L,
    ENDS_AA_HAS_L,
    HAS_L,
    NO_STATE
  }

  private static void displayState(Map<WinningStates, Long> currentState, int i)
  {
    long total = 0;

    // Total up the
    for (Long count : currentState.values())
    {
      total += count;
    }

    System.out.println("Count for " + i + " = " + total + "; state map:");
    for (WinningStates winningStates : currentState.keySet())
    {
      // not necessary, but useful to demonstate for other people how the code works
      System.out.println("  " + winningStates + "->" + currentState.get(winningStates));
    }

  }

  private static void addToExisting(Map<WinningStates, Long> oldStateMap,
                                    Map<WinningStates, Long> newStateMap,
                                    WinningStates oldState,
                                    WinningStates newState)
  {
    Long oldCount = oldStateMap.get(oldState);
    if (oldCount == null)
    {
      oldCount = 0L;
    }

    Long currCount = newStateMap.get(newState);
    if (currCount == null)
    {
      currCount = 0L;
    }

    newStateMap.put(newState, oldCount + currCount);
  }

  static Map<WinningStates, Long> nextState(Map<WinningStates, Long> lastStateMap)
  {
    Map<WinningStates, Long> newStateMap = new EnumMap<WinningStates, Long>(WinningStates.class);

    for (WinningStates oldState : lastStateMap.keySet())
    {
      switch (oldState)
      {
        case ENDS_WITH_A_NO_L:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.ENDS_WITH_AA_NO_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.NO_STATE);
          break;

        case ENDS_WITH_AA_NO_L:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.NO_STATE);
          break;

        case ENDS_A_HAS_L:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.ENDS_AA_HAS_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          break;

        case ENDS_AA_HAS_L:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          break;

        case HAS_L:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.ENDS_A_HAS_L);
          break;

        case NO_STATE:
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.NO_STATE);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.HAS_L);
          addToExisting(lastStateMap, newStateMap, oldState, WinningStates.ENDS_WITH_A_NO_L);
          break;
      }
    }
    return newStateMap;
  }

  public static void main(String[] args)
  {
    // prime the pump:
    Map<WinningStates, Long> lastState = new EnumMap<WinningStates, Long>(WinningStates.class);
    lastState.put(WinningStates.ENDS_WITH_A_NO_L, 1L);
    lastState.put(WinningStates.HAS_L, 1L);
    lastState.put(WinningStates.NO_STATE, 1L);
    displayState(lastState, 1);


    for (int i = 2; i <= 30; i++)
    {
      Map<WinningStates, Long> nextState = nextState(lastState);
      displayState(nextState, i);
      lastState = nextState;
    }
  }
}
