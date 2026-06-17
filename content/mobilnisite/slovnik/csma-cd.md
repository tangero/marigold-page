---
slug: "csma-cd"
url: "/mobilnisite/slovnik/csma-cd/"
type: "slovnik"
title: "CSMA/CD – Carrier Sense Multiple Access with Collision Detection"
date: 2025-01-01
abbr: "CSMA/CD"
fullName: "Carrier Sense Multiple Access with Collision Detection"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csma-cd/"
summary: "CSMA/CD je metoda řízení přístupu k médiu (MAC) používaná v drátových sítích Ethernet, kde zařízení před vysíláním naslouchají a detekují kolize. Ve specifikacích 3GPP je na ni odkazováno v integrační"
---

CSMA/CD je metoda přístupu k síti Ethernet odkazovaná ve specifikacích 3GPP pro integrační scénáře, umožňující celulárním systémům propojení s tradičními drátovými sítěmi LAN, které pro jednotnou správu sítě využívají detekci kolizí.

## Popis

Carrier Sense [Multiple Access](/mobilnisite/slovnik/multiple-access/) with Collision Detection (CSMA/[CD](/mobilnisite/slovnik/cd/)) je základní protokol pro správu přístupu ke sdílenému přenosovému médiu v lokálních sítích ([LAN](/mobilnisite/slovnik/lan/)). Protokol funguje na vrstvě datových spojů (vrstva 2) modelu [OSI](/mobilnisite/slovnik/osi/), konkrétně v podsublayer Media Access Control ([MAC](/mobilnisite/slovnik/mac/)). Jeho hlavní funkcí je regulovat, jak více zařízení sdílí společný komunikační kanál, jako je koaxiální kabel nebo segment kroucené dvoulinky Ethernetu, předcházet kolizím dat a zajišťovat efektivní přenos dat.

Operační mechanismus CSMA/CD sleduje specifickou sekvenci. Nejprve zařízení s daty k odeslání provede 'Carrier Sense' – naslouchá médiu, aby zjistilo, zda právě probíhá jiný přenos. Pokud je médium volné, zařízení začne vysílat svůj datový rámec. Během vysílání současně provádí 'Collision Detection' sledováním signálu na médiu. Pokud zařízení detekuje odlišný signál (což naznačuje, že jiné zařízení začalo vysílat současně), došlo ke kolizi. Po detekci kolize zařízení okamžitě zastaví přenos a vyšle jam signál, aby zajistilo, že všechny ostatní stanice kolizi rozpoznají. Zařízení poté implementuje 'backoff algoritmus' – čeká náhodnou dobu před pokusem o opětovný přenos, čímž snižuje pravděpodobnost opakovaných kolizí.

Klíčové součásti systému CSMA/CD zahrnují transceiver fyzické vrstvy, který zajišťuje přenos signálu a detekci kolizí; řadič MAC, který implementuje algoritmy naslouchání nosné, detekce kolizí a backoff; a strukturu rámce, která zahrnuje preambuli, cílové/zdrojové adresy, datovou část a kontrolní sekvenci rámce. Backoff algoritmus typicky používá binární exponenciální backoff, kde čekací doba se s každou následující kolizí zdvojnásobuje až do maximálního limitu, což poskytuje dynamické přizpůsobení úrovni síťového vytížení.

V rámci architektury 3GPP se CSMA/CD nepoužívá v rádiové přístupové síti, ale objevuje se ve specifikacích, jako je 29.561, pro scénáře zahrnující spolupráci s ne-3GPP přístupovými sítěmi. To zahrnuje integraci s drátovými Ethernetovými backhaulovými spoji, průmyslovými sítěmi nebo staršími systémy, kde je nasazen Ethernet založený na CSMA/CD. Systém 3GPP musí brát v úvahu charakteristiky sítí CSMA/CD při správě kvality služeb (QoS), přechodech mezi buňkami nebo bezpečnostních politikách napříč těmito heterogenními typy přístupu, aby zajistil bezproblémovou kontinuitu služeb mezi celulární a drátovou doménou.

## K čemu slouží

CSMA/[CD](/mobilnisite/slovnik/cd/) byl vytvořen k řešení základního problému více zařízení soutěžících o přístup ke sdílenému komunikačnímu médiu v raných lokálních sítích. Před CSMA/CD síťové návrhy často používaly mechanismy předávání tokenu nebo dotazování, které zaváděly latenci a složitost, zejména s růstem velikosti sítě. CSMA/CD poskytl decentralizovaný, distribuovaný přístup, kde každé zařízení nezávisle spravovalo svůj přístup, čímž odpadla potřeba centrálního arbitra a sítě se staly škálovatelnějšími a odolnějšími vůči poruchám.

Protokol konkrétně řeší problém '[multiple access](/mobilnisite/slovnik/multiple-access/)' – jak umožnit několika zařízením efektivně sdílet jeden vysílací kanál. Složka 'carrier sense' předchází kolizím tam, kde je to možné, tím, že zařízení před vysíláním kontrolují dostupnost kanálu. Složka 'collision detection' poskytuje mechanismus obnovy pro případy, kdy ke kolizím nevyhnutelně dojde kvůli zpoždění šíření (době, kterou signál potřebuje k průchodu kabelem). Bez detekce kolizí by se přenos poškozených rámců dál pokračoval, plýtvalo by se šířkou pásma a protokoly vyšších vrstev by musely řešit opakované přenosy po vypršení časového limitu, což by výrazně snížilo efektivitu.

V kontextu standardů 3GPP není účelem CSMA/CD definovat protokoly celulárního rozhraní, ale umožnit integraci s existující infrastrukturou drátových sítí. Jak se systémy 3GPP vyvíjely, aby podporovaly integraci s ne-3GPP přístupem (jako jsou drátové sítě v 5G), porozumění CSMA/CD se stalo nezbytným pro správu koncových spojení, která procházejí jak celulárními, tak tradičními ethernetovými segmenty. To operátorům umožňuje využít stávající infrastrukturu při poskytování konzistentních služeb, zejména pro pevný bezdrátový přístup, podnikovou konektivitu a nasazení průmyslového IoT, kde se konvergují drátové a bezdrátové technologie.

## Klíčové vlastnosti

- Naslouchání nosné před vysíláním pro kontrolu dostupnosti média
- Současné vysílání a detekce kolizí na sdíleném médiu
- Okamžité zastavení přenosu po detekci kolize
- Vysílání jam signálu k oznámení kolize všem stanicím
- Binární exponenciální backoff algoritmus pro načasování opakovaného přenosu
- Decentralizované řízení přístupu k médiu bez centrálního koordinátora

## Definující specifikace

- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [CSMA/CD na 3GPP Explorer](https://3gpp-explorer.com/glossary/csma-cd/)
