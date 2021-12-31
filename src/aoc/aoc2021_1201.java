package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class aoc2021_1201
{
  public static class Node
  {
    String name;
    List<Node> neighbors;
    boolean large = false;

    public Node(String name)
    {
      this.name = name;
      neighbors = new ArrayList<>();

      if (name.toUpperCase().equals(name))
      {
        large = true;
      }
    }

    public void addNeighbor(Node neighbor)
    {
      if (!neighbors.contains(neighbor))
      {
        neighbors.add(neighbor);
      }
    }

    public String getName()
    {
      return name;
    }

    public boolean isLarge()
    {
      return large;
    }

    public List<Node> getNeighbors()
    {
      return neighbors;
    }
  }

  public static class NodeMap
  {
    Map<String, Node> nodeMap;

    public NodeMap()
    {
      nodeMap = new HashMap<>();
    }

    public void addConnection(String route)
    {
      String[] nodeString = route.split("-");

      String leftString = nodeString[0];
      String rightString = nodeString[1];
      Node leftNode = nodeMap.get(leftString);
      Node rightNode = nodeMap.get(rightString);

      if (leftNode == null)
      {
        leftNode = new Node(leftString);
        nodeMap.put(leftString, leftNode);
      }

      if (rightNode == null)
      {
        rightNode = new Node(rightString);
        nodeMap.put(rightString, rightNode);
      }

      leftNode.addNeighbor(rightNode);
      rightNode.addNeighbor(leftNode);
    }

    public Node getStartNode()
    {
      return nodeMap.get("start");
    }

    public Node getEndNode()
    {
      return nodeMap.get("end");
    }

    @Override
    public String toString()
    {
      return "NodeMap{" +
          "nodeMap=" + nodeMap +
          '}';
    }
  }

  public aoc2021_1201(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    NodeMap nodeMap = new NodeMap();
    for (String line : lines)
    {
      nodeMap.addConnection(line);
    }

    System.out.println("nodeMap = " + nodeMap);

    List<List<Node>> partialPaths = new ArrayList<>();
    List<Node> startPath = new ArrayList<>(Collections.singletonList(nodeMap.getStartNode()));
    partialPaths.add(startPath);

    List<List<Node>> endingPaths = new ArrayList<>();

    while (!partialPaths.isEmpty())
    {
      List<List<Node>> newPaths = new ArrayList<>();
      for (List<Node> path : partialPaths)
      {
        Node lastRoom = path.get(path.size() - 1);
        List<Node> neighbors = lastRoom.getNeighbors();
        for (Node neighbor : neighbors)
        {
          if (neighbor == nodeMap.getEndNode())
          {
            List<Node> endingPath = new ArrayList<>(path);
            endingPath.add(neighbor);
            endingPaths.add(endingPath);
          }
          else if (neighbor.isLarge() || !path.contains(neighbor))
          {
            List<Node> newPath = new ArrayList<>(path);
            newPath.add(neighbor);
            newPaths.add(newPath);
          }
        }
      }
      partialPaths = newPaths;
    }
    System.out.println("number of paths = " + endingPaths.size());
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_1201 me = new aoc2021_1201("aoc2021_1201_testinput.txt"); // expect 10
//      aoc2021_1201 me = new aoc2021_1201("aoc2021_1201_testinput2.txt"); // expect 19
//      aoc2021_1201 me = new aoc2021_1201("aoc2021_1201_testinput3.txt"); // expect 226
      aoc2021_1201 me = new aoc2021_1201("aoc2021_1201_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
