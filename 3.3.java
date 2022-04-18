import java.util.*;
class Resultado {
    int vencedor;
    int perdedor;
  
    Resultado(int vencedor, int perdedor)
    {
        this.vencedor = vencedor;
        this.perdedor = perdedor;
    }
}

class MapearTimes {
  
 
    static void mapearTimes(int[] times,
                             Resultado[] resultados)
    {
        HashMap<Integer,
                List<Integer> >
            map = new HashMap<>();
        int vencedor = 0;
  
       
        for (int i = 0; i < resultados.length; i++) {
            vencedor = resultados[i].vencedor;
            if (map.containsKey(vencedor)) {
                map.get(vencedor).add(
                    resultados[i].perdedor);
            }
            else {
                List<Integer> list
                    = new ArrayList<Integer>();
                list.add(resultados[i].perdedor);
                map.put(vencedor, list);
            }
        }
        List<Integer> sequencia = new ArrayList<>();
  
       
        ordenarTimes(times, map, times.length, sequencia);
        Iterator<Integer> it = sequencia.iterator();
  
       
        System.out.print("\n");
        while (it.hasNext()) {
            System.out.print(it.next());
            System.out.print(" ");
        }
    }
  
  
    static void ordenarTimes(
        int[] times,
        HashMap<Integer, List<Integer> > map,
        int n, List<Integer> sequencia)
    {
    
        if (n < 1) {
            return;
        }
        else if (n == 1) {
            System.out.print("n == 1 -> " + times[n-1]);
            sequencia.add(times[n - 1]);
            
            return;
        }
  
        //Chamada recursiva para gerar um sequencia de N-1 times
        System.out.print("n antes recursao = "+n+"\n");
        ordenarTimes(times, map, n - 1, sequencia);
        int chave = times[n - 1];
        int i;
        System.out.print("\n\n n depois recursao= "+ n + "\n");
        //Achando a posição do time atual na lista de sequencia
        for (i = 0; i < sequencia.size(); i++) {
  
            
            //Pega o time no indice atual na lista
           System.out.print("i = "+i+" -> chave = "+chave+" -> ");
            int team = sequencia.get(i);
            System.out.print("Team = Output("+i+") = "+sequencia.get(i)+" -> Map = ");
  
            // Checa se perdeu para o time atual
            List<Integer> perdedores = map.get(chave);
            System.out.print(map.get(chave));
            System.out.print("\n");
            if (perdedores.indexOf(team) != -1)
                System.out.print("ganhou de "+team+", entao "+chave+ " fica na frente de "+team+"\n");
            if (perdedores.indexOf(team) != -1)
                break;
        }
        //Adiciona o time atual na posição i
        System.out.print("Adicionado ao sequencia i = "+i+" chave = "+chave);
        sequencia.add(i, chave);
        return; 
    }
  
    
    public static void main(String[] args)
    {
        int[] times = { 1, 2, 3, 4 };
        Resultado[] resultados = {
            new Resultado(1, 4),
            new Resultado(4, 3),
            new Resultado(2, 3),
            new Resultado(1, 2),
            new Resultado(2, 1),
            new Resultado(3, 1),
            new Resultado(2, 4)
        };
  
        
        mapearTimes(times, resultados);
    }
}