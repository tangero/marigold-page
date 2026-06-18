---
slug: "pcntr"
url: "/mobilnisite/slovnik/pcntr/"
type: "slovnik"
title: "PCNTR – Padding Counter"
date: 2002-01-01
abbr: "PCNTR"
fullName: "Padding Counter"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pcntr/"
summary: "Čítač používaný v bezpečnostních algoritmech 3GPP (konkrétně šifrovacím algoritmu f8) pro generování unikátního bloku šifrovacího klíče pro každý rámec. Zabrání opakovanému použití stejného šifrovacíh"
---

PCNTR (čítač doplňování) je čítač používaný v šifrovacím algoritmu 3GPP f8 pro generování unikátního bloku šifrovacího klíče pro každý rámec, čímž zabraňuje opakovanému použití šifrovacího klíče a zajišťuje důvěrnost dat přes rozhraní vzdušného rozhraní.

## Popis

Padding Counter (PCNTR, čítač doplňování) je bezpečnostní parametr definovaný ve specifikaci 3GPP pro algoritmus důvěrnosti f8, který se používá pro šifrování v UMTS a pozdějších systémech. Algoritmus f8 je proudová šifra, která generuje pseudonáhodný šifrovací klíč, jenž je následně kombinován operací XOR s otevřeným textem za vzniku šifrovaného textu. PCNTR je klíčovým vstupem do algoritmu f8 a zajišťuje, že šifrovací klíč je unikátní pro každý rádiový rámec, čímž zabraňuje útokům založeným na opakovaném použití šifrovacího klíče.

Z architektonického hlediska bere algoritmus f8 několik vstupů: klíč důvěrnosti ([CK](/mobilnisite/slovnik/ck/)), časově závislý vstup nazývaný [COUNT-C](/mobilnisite/slovnik/count-c/) (32bitové pořadové číslo), identifikátor přenašeče (BEARER), směr přenosu (DIRECTION) a požadovanou délku šifrovacího klíče (LENGTH). Protože však standardní velikost rádiového bloku nemusí přesně odpovídat velikosti bloku šifrovacího klíče generovaného podkladovým základním algoritmem (KASUMI v určitém režimu), je někdy nutné doplnění. PCNTR je 5bitový čítač (hodnoty 0-31), který se zvyšuje pro každý následující blok šifrovacího klíče generovaný v rámci jednoho rádiového rámce pro splnění jedné šifrovací žádosti. Jeho primární role je poskytovat variaci mezi těmito po sobě jdoucími bloky šifrovacího klíče.

Princip fungování: Když UE nebo síť potřebuje zašifrovat rádiový blok, vyvolá algoritmus f8. Algoritmus interně používá blokovou šifru KASUMI v režimu podobném výstupní zpětné vazbě pro generování šifrovacího klíče. Vstup do KASUMI zahrnuje upravenou verzi COUNT-C. Pro první blok šifrovacího klíče rámce je PCNTR nastaven na nulu. Algoritmus vyprodukuje 64bitový výstupní blok. Pokud je potřeba více bitů šifrovacího klíče (protože rádiový blok je větší než 64 bitů), je PCNTR zvýšen a algoritmus je spuštěn znovu se stejnými ostatními vstupy, ale se zvýšenou hodnotou PCNTR. Tím se vygeneruje další 64bitový blok šifrovacího klíče. Tento proces se opakuje, dokud není vygenerováno dostatek bitů šifrovacího klíče pro pokrytí celého otevřeného textu. Unikátnost PCNTR pro každý blok v rámci rámce zajišťuje, že stejný segment šifrovacího klíče se nikdy neopakuje, a to ani v rámci stejné šifrovací relace pro jeden rámec.

Klíčovými součástmi jsou klíč důvěrnosti (CK), který je odvozen během autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)), a COUNT-C, což je čítač závislý na rámci, který se mění pro každý nový rádiový rámec. PCNTR funguje ve spojení s COUNT-C. Zatímco COUNT-C poskytuje unikátnost napříč různými rámci a časovými obdobími, PCNTR poskytuje unikátnost napříč různými bloky v rámci stejného rámce. Tento dvouúrovňový systém čítačů je robustní obranou proti útokům využívajícím opakování šifrovacího klíče. Role PCNTR je tedy nízkoúrovňový, nezbytný mechanismus v rámci šifrovacího procesu, který podporuje sémantickou bezpečnost komunikace a zajišťuje, že i když jsou stejná data odeslána ve dvou různých blocích stejného rámce, šifrovaný text bude odlišný.

## K čemu slouží

Padding Counter existuje, aby řešil specifický kryptografický problém v návrhu proudové šifry f8: zabránění internímu generátoru šifrovacího klíče ve vytváření identických výstupních bloků během šifrování jedné, potenciálně dlouhé, zprávy (rádiového rámce). U proudové šifry, pokud je stejný šifrovací klíč použit pro zašifrování dvou různých bloků otevřeného textu, může to vést ke katastrofálním bezpečnostním selháním. Útočník by mohl aplikovat operaci XOR na dva šifrované texty, čímž by odstranil šifrovací klíč a odhalil informace o otevřených textech.

Historická a technická motivace vychází z použití blokové šifry (KASUMI) v režimu, který ji mění na generátor šifrovacího klíče. Bloková šifra sama o sobě produkuje pro daný vstup výstup pevné velikosti. Pro generování dlouhého šifrovacího klíče se režim musí opakovat. Pouhé opakování stejného vstupu by opakovaně produkovalo stejný výstupní blok, což je nebezpečné. Proto je interní čítač jako PCNTR zaveden jako součást vstupu do blokové šifry pro každou iteraci, čímž se zajistí, že každý 64bitový blok šifrovacího klíče je unikátní. Jedná se o standardní techniku v kryptografických režimech, jako je [CTR](/mobilnisite/slovnik/ctr/) (Counter Mode) nebo [OFB](/mobilnisite/slovnik/ofb/) (Output Feedback).

V kontextu bezpečnosti 3GPP UMTS byl algoritmus f8 navržen tak, aby poskytoval silnou důvěrnost. PCNTR spolu s čítačem rámců ([COUNT-C](/mobilnisite/slovnik/count-c/)) řeší omezení dřívějších, méně robustních šifrovacích schémat (jako algoritmy A5 v GSM), která byla zranitelná vůči různým útokům. Tím, že zaručuje unikátnost šifrovacího klíče napříč časem (rámci) i prostorem (bloky v rámci rámce), pomáhá PCNTR zajistit, aby algoritmus f8 splňoval svůj návrhový cíl být bezpečnou proudovou šifrou pro náročné prostředí mobilních komunikací, kde jsou obrovská množství dat šifrována stejným dlouhodobým klíčem ([CK](/mobilnisite/slovnik/ck/)).

## Klíčové vlastnosti

- 5bitový čítač (0-31) zajišťující unikátnost bloků šifrovacího klíče v rámci jednoho rádiového rámce
- Integrální vstupní parametr algoritmu důvěrnosti 3GPP f8
- Funguje ve spojení s čítačem rámců (COUNT-C) a poskytuje dvouvrstvou záruku unikátnosti
- Zabraňuje opakování šifrovacího klíče, což je kritický požadavek pro bezpečnost proudových šifer
- Sekvenčně se zvyšuje pokaždé, když je pro danou šifrovací operaci vygenerován nový 64bitový blok šifrovacího klíče
- Transparentní pro vyšší vrstvy; spravován interně kryptografickou implementací v UE a RNC

## Související pojmy

- [COUNT-C – Ciphering Sequence Number for Core Network](/mobilnisite/slovnik/count-c/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [PCNTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcntr/)
