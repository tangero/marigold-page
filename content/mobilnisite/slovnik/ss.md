---
slug: "ss"
url: "/mobilnisite/slovnik/ss/"
type: "slovnik"
title: "SS – Supplementary Services"
date: 2026-01-01
abbr: "SS"
fullName: "Supplementary Services"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ss/"
summary: "Doplňkové služby (SS) jsou sada pokročilých telefonních funkcí, které rozšiřují základní možnosti hovorů v mobilních sítích s přepojováním okruhů (GSM, UMTS) a v IMS. Zahrnují služby jako Přesměrování"
---

SS je sada pokročilých telefonních funkcí, jako je přesměrování hovoru a čekání na hovor, které rozšiřují základní možnosti hovorů v sítích s přepojováním okruhů a v IMS a poskytují tak uživateli bohatší zážitek.

## Popis

Doplňkové služby (SS) představují komplexní portfolio přidaných telefonních funkcí definovaných ve standardech 3GPP, které fungují ve spojení se základní telekomunikační službou, což je primárně zřízení a udržování dvoustranného hlasového hovoru. Jsou základním kamenem tradičních mobilních sítí s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako jsou GSM a UMTS, a jejich principy a mnohé konkrétní služby byly přeneseny do IP Multimedia Subsystem (IMS) pro VoLTE a VoNR. SS nějakým způsobem upravují, rozšiřují nebo omezují základní hovor, aby poskytly uživatelům větší kontrolu, soukromí a funkcionalitu.

Z architektonického hlediska jsou v klasických sítích GSM/UMTS CS doplňkové služby spravovány Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a prováděny Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)). HLR ukládá údaje o předplatném SS účastníka, včetně povolených služeb a jejich konkrétních parametrů (např. číslo pro přesměrování u Přesměrování hovoru bez podmínek). Když se účastník registruje v síti, tato data jsou přenesena do VLR, který tohoto účastníka obsluhuje. MSC/VLR následně aplikuje logiku těchto služeb během fáze sestavování hovoru a během hovoru. Signalizace pro aktivaci, deaktivaci a dotazování na SS používá protokol Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) mezi HLR a VLR a pro interakci s účastníkem se často používají [DTMF](/mobilnisite/slovnik/dtmf/) tóny nebo kódy nestrukturovaných doplňkových služeb ([USSD](/mobilnisite/slovnik/ussd/)).

V doméně IMS pro VoLTE/VoNR jsou doplňkové služby implementovány pomocí metod a balíčků událostí [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), což odpovídá IP povaze IMS. Servisní logika často sídlí v aplikačním serveru (AS) uvnitř jádra IMS. Například službu Přesměrování hovoru v IMS by zpracovával SIP AS, který zachytí požadavky INVITE, zkontroluje pravidla přesměrování účastníka a případně hovor přesměruje. Tradiční SS ve stylu CS jsou mapovány na ekvivalentní komunikační služby IMS, čímž je zajištěna funkční parita a hladká migrace pro účastníky. Správa nastavení SS v IMS může být provedena přes rozhraní Ut (pomocí protokolu XCAP), což uživateli umožňuje konfigurovat služby přes webový portál.

Provoz konkrétní doplňkové služby zahrnuje dobře definovaný stavový model a procedury. Vezměme si jako příklad Čekání na hovor: když je účastník (Uživatel B) v probíhajícím hovoru a přijde nový příchozí hovor, MSC (nebo IMS AS) zjistí, že je pro Uživatele B aktivní Čekání na hovor. Namísto odmítnutí nového hovoru obsazeným signálem MSC/AS přehraje do stávajícího spojení tón čekání na hovor a odešle oznámení (např. SIP re-INVITE s hlavičkou alert-info) do UE Uživatele B. UE pak uživateli poskytne indikaci a ten se může rozhodnout přerušit první hovor a přijmout druhý, čímž vyvolá doplňkovou službu Podržení hovoru. To ukazuje, jak může více SS interagovat a vytvořit složitý uživatelský zážitek. Další kritickou kategorií je Blokování hovorů, které zahrnuje služby jako Blokování všech odchozích hovorů (BAOC) nebo Blokování příchozích hovorů při roamingu (BIC-Roam), které jsou klíčové pro zabezpečení a kontrolu nákladů, zejména v roamingu.

## K čemu slouží

Doplňkové služby byly vytvořeny za účelem proměnit mobilní telefon z jednoduchého bezdrátového hlasového kanálu v sofistikovaný osobní komunikační nástroj, který se vyrovná a nakonec překoná sadu funkcí pevné telefonní sítě (PSTN/ISDN). Základní telekomunikační služba poskytuje pouze sestavení spojení a přenos hlasu. SS přidávají inteligenci a uživatelskou kontrolu nezbytnou pro praktické každodenní použití, jako je správa více hovorů, ochrana soukromí a přizpůsobení zacházení s hovory na základě času nebo identity volajícího.

Historicky byl vývoj SS v GSM (počínaje Fází 1 a výrazně rozšířen ve Fázi 2) hnán potřebou standardizace mezi různými operátory a zeměmi, aby bylo možné bezproblémové roamování a interoperabilitu. Bez standardizovaných SS by funkce jako Přesměrování hovoru mohla fungovat v domovské síti účastníka, ale selhat při roamingu, což by vedlo k roztříštěnému uživatelskému zážitku. Specifikace 3GPP poskytly společnou sadu funkcí, protokolů a rozhraní, což zajistilo, že služba jako Zobrazení identifikace volající linky (CLIP) bude fungovat konzistentně bez ohledu na navštívenou síť.

Dále se SS staly významným zdrojem příjmů a diferenciace pro operátory. Mohli nabízet služby v různých balíčcích a účtovat si příplatek za pokročilé funkce, jako je konference s více účastníky nebo explicitní přenos hovoru. Poskytovaly také nezbytné nástroje pro účastníky: služby Blokování hovorů umožnily rodičům kontrolovat používání telefonu dětmi nebo firmám spravovat oprávnění zaměstnanců k volání. Přesměrování hovoru umožnilo funkci „sleduj mě“. Jak se sítě vyvíjely směrem k IMS a VoIP, bylo nezbytné zachovat tuto bohatou sadu funkcí, aby byla zajištěna uživatelská přijatelnost nové technologie. Proto hlavním cílem návrhu IMS bylo podporovat ekvivalentní nebo vylepšené doplňkové služby, čímž se řešil problém regrese funkcí při migraci z CS hlasu na VoLTE/VoNR, a tím se chránil jak uživatelský zážitek, tak příjmy operátora z poskytovaných služeb.

## Klíčové vlastnosti

- Standardizovaná sada pokročilých funkcí hovoru včetně Přesměrování hovoru (bez podmínek, při obsazení, při nezvednutí), Blokování hovorů (odchozích, příchozích, při roamingu), Čekání na hovor, Podržení hovoru
- Zobrazení identifikace volající linky (CLIP) a Omezení identifikace volající linky (CLIR) pro správu čísla volajícího
- Služba Komunikace s více účastníky (Konference) pro sestavení hovoru s více než dvěma stranami
- Explicitní přenos hovoru (ECT) umožňující uživateli přenést sestavený hovor na třetí stranu
- Uzavřená skupina uživatelů (CUG) umožňující vytváření privátních skupin pro hovory v rámci sítě
- Implementováno jak v jádru s přepojováním okruhů (MSC/HLR), tak v IMS (SIP aplikační servery) s definovanou vzájemnou spoluprací

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.424** (Rel-19) — XCAP over Ut for Supplementary Services MO
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 26.130** (Rel-19) — RTP Payload Format Testing for 3GPP Codecs
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- … a dalších 162 specifikací

---

📖 **Anglický originál a plná specifikace:** [SS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss/)
