---
slug: "rach"
url: "/mobilnisite/slovnik/rach/"
type: "slovnik"
title: "RACH – Random Access Channel"
date: 2025-01-01
abbr: "RACH"
fullName: "Random Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rach/"
summary: "Sdílený uplinkový kanál používaný UE k zahájení komunikace se sítí, když nejsou synchronizovány. Je klíčový pro počáteční přístup k síti, navázání spojení, handovery a žádosti o uplinkovou synchroniza"
---

RACH je sdílený uplinkový kanál, který používají UE k zahájení komunikace se sítí, když nejsou synchronizovány, a umožňuje tak počáteční přístup, navázání spojení, handovery a žádosti o synchronizaci.

## Popis

Náhodný přístupový kanál (Random Access Channel – RACH) je základní uplinkový transportní kanál v 3GPP rádiových přístupových sítích ([UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/) a NG-RAN). Je to kanál založený na soutěžení (contention-based), což znamená, že více uživatelských zařízení (UE) se o něj může pokusit získat přístup současně, což může vést ke kolizím vyžadujícím procedury řešení. Primárním účelem RACH je umožnit UE, které ještě není časově synchronizováno s uplinkovým časováním sítě, požádat o počáteční spojení, provést handover, znovu navázat spojení po selhání rádiového spoje nebo požádat o uplinkové prostředky pro plánovací žádosti ([SR](/mobilnisite/slovnik/sr/)), když nejsou nakonfigurovány vyhrazené SR prostředky.

Procedura RACH, často nazývaná náhodný přístup (Random Access – [RA](/mobilnisite/slovnik/ra/)), je vícekrokový proces. V LTE a NR existuje ve dvou hlavních formách: soutěžní náhodný přístup (Contention-Based Random Access – [CBRA](/mobilnisite/slovnik/cbra/)) a nesoutěžní náhodný přístup (Contention-Free Random Access – [CFRA](/mobilnisite/slovnik/cfra/)). Při CBRA UE náhodně vybere preambuli (specifickou signálovou sekvenci) ze sady vysílané gNB/[eNB](/mobilnisite/slovnik/enb/) a odešle ji na fyzickém náhodném přístupovém kanálu ([PRACH](/mobilnisite/slovnik/prach/)). Síť po detekci preambule odpoví zprávou odezvy na náhodný přístup (Random Access Response – RAR) obsahující dočasný identifikátor (TC-RNTI), příkaz časového předstihu (timing advance) pro synchronizaci a počáteční uplinkový grant pro UE, aby mohlo odeslat naplánovanou zprávu (např. RRC Connection Request). Pokud více UE vybere stejnou preambuli současně, dojde ke kolizi, která je vyřešena v následné výměně zpráv. CFRA se používá ve scénářích jako je handover, kde síť předem přidělí UE vyhrazenou preambuli, aby se předešlo soutěžení.

Z architektonického hlediska je RACH mapován na fyzický náhodný přístupový kanál (Physical Random Access Channel – PRACH). Konfigurace PRACH, včetně dostupných formátů preambulí, časových/frekvenčních prostředků (RACH příležitostí) a kořenových sekvencí, je vysílána v systémové informaci (SIB1/SIB2 v LTE, SIB1 v NR). Fyzická vrstva UE se stará o přenos preambule, zatímco vyšší vrstvy (MAC a RRC) spravují logiku procedury, backoff a řešení selhání. Návrh formátů preambulí (např. s různou délkou) podporuje různé velikosti buněk a scénáře nasazení, od malých buněk po velké venkovské buňky, tím, že zohledňuje různá zpoždění doby zpátečního šíření.

V celkovém provozu sítě je RACH kritickým prvním krokem pro UE přecházející z režimu idle (RRC_IDLE) nebo inactive (RRC_INACTIVE) do režimu connected (RRC_CONNECTED). Je také zásadní pro udržování uplinkové synchronizace, protože časový předstih (timing advance) poskytnutý v RAR zajišťuje ortogonální uplinkové přenosy od více UE a předchází tak interferenci. V 5G NR byly zavedeny vylepšení jako 2-step RACH, kde UE kombinuje preambuli (MsgA) a naplánovanou zprávu (jako Msg3) do jediného přenosu, čímž se snižuje latence přístupu, což je klíčové pro případy použití ultra-spolehlivé nízkolatenční komunikace (URLLC).

## K čemu slouží

RACH byl vytvořen, aby vyřešil základní problém, jak může nesynchronizované UE počátečně kontaktovat mobilní síť bez předchozí koordinace. V raných mobilních systémech, bez mechanismu pro uplinkovou synchronizaci, by současné přenosy od více UE způsobily vážné interference, což by činilo síťový přístup nespolehlivým. RACH poskytuje strukturovanou, soutěžení řízenou metodu pro tento počáteční kontakt, umožňující efektivní sdílení rádiového média.

Jeho návrh řeší výzvu náhodného přístupu ve sdíleném médiu (rozhraní vzduchu). Použitím krátkých, detekovatelných sekvencí preambulí může síť efektivně detekovat pokusy o přístup i při špatném časovém zarovnání. Mechanismus řešení kolizí umožňuje síti elegantně zvládat kolize, které jsou v systému s mnoha potenciálními uživateli nevyhnutelné. To je mnohem efektivnější než vyhrazené signalizační kanály pro každé potenciální UE, které by plýtvaly cennými rádiovými prostředky.

Během generací se jeho účel rozšířil za pouhý počáteční přístup. Nyní podporuje klíčové funkce mobility jako handover, kdy se UE potřebuje rychle synchronizovat s novou buňkou. Slouží také pro uplinkové plánovací žádosti, když má UE data k odeslání, ale nemá vyhrazený řídicí kanál. Vývoj směrem k nižší latenci, zejména v 5G, podnítil vylepšení jako 2-step RACH, která přířečně řeší potřebu rychlejšího navázání spojení v aplikacích pro kritickou infrastrukturu a průmyslový IoT.

## Klíčové vlastnosti

- Režimy přístupu se soutěžením (contention-based) a bez soutěžení (contention-free)
- Uplinková časová synchronizace prostřednictvím příkazu časového předstihu (Timing Advance)
- Mechanismy detekce a řešení kolizí
- Konfigurovatelné formáty preambulí pro různé velikosti buněk
- Podpora počátečního přístupu, handoveru a plánovacích žádostí
- Nízkolatenční procedura náhodného přístupu ve dvou krocích (2-step random access) (5G NR)

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- … a dalších 36 specifikací

---

📖 **Anglický originál a plná specifikace:** [RACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/rach/)
