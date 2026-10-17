# Diagrama Esquemático de Interconexión Eléctrica y de Potencia — STR-002 H3

========================================================================================
                 DIAGRAMA DE INTERCONEXIÓN ELÉCTRICA Y DE POTENCIA — STR-002 H3
========================================================================================

  [ Batería Inteligente HV 18S ] (30 Ah, 66.6V Nominal)
         │
         ├── Conectores QS8-S Anti-Spark & Cableado Principal 10-12 AWG
         ▼
  [ Módulo Distribuidor de Potencia PDB Principal (Alta Corriente ~126 A) ]
         │
         ├──► [ Banco de Potencia - Motores (1 al 8) ]
         │      │
         │      ├── PDB Splitter Bus 18S
         │      │     ├── ESC 1 (40A-60A Opt.) ──► Motor Brushless 1 (Hélice 30")
         │      │     ├── ESC 2 (40A-60A Opt.) ──► Motor Brushless 2 (Hélice 30")
         │      │     ├── ESC 3 (40A-60A Opt.) ──► Motor Brushless 3 (Hélice 30")
         │      │     └── ESC 4 (40A-60A Opt.) ──► Motor Brushless 4 (Hélice 30")
         │      │
         │      └── PDB Splitter Bus 18S (Lado Opuesto)
         │            ├── ESC 5 (40A-60A Opt.) ──► Motor Brushless 5 (Hélice 30")
         │            ├── ESC 6 (40A-60A Opt.) ──► Motor Brushless 6 (Hélice 30")
         │            ├── ESC 7 (40A-60A Opt.) ──► Motor Brushless 7 (Hélice 30")
         │            └── ESC 8 (40A-60A Opt.) ──► Motor Brushless 8 (Hélice 30")
         │
         └──► [ Módulo de Conversión DC-DC (Step-Down HV a 12V / 24V) ]
                │
                ├──► [ Aviónica y Control de Vuelo Principal (Pixhawk / Cube Orange+) ]
                │      ├── Módulo GPS / RTK GNSS Dual
                │      ├── Telemetría de Alta Frecuencia (SigCom / LTE)
                │      └── Radar Phased-Array 3D (77-81 GHz) & Visión Estéreo 360°
                │
                └──► [ Sistema Hidráulico CDA & Control Periférico ]
                       ├── Bomba de Diafragma / Dosificadora VRA
                       └── 2x Atomizadores Centrifugos de Gota Variable (80-600 µm)
========================================================================================
