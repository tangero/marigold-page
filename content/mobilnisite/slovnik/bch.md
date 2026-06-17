---
slug: "bch"
url: "/mobilnisite/slovnik/bch/"
type: "slovnik"
title: "BCH – Bose-Chaudhuri-Hocquenghem Code"
date: 2025-01-01
abbr: "BCH"
fullName: "Bose-Chaudhuri-Hocquenghem Code"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bch/"
summary: "BCH (Bose-Chaudhuri-Hocquenghemův kód) je třída výkonných cyklických kódů pro opravu chyb používaných v systémech 3GPP pro dopřednou korekci chyb (FEC). Je klíčový pro ochranu vysílacích a řídicích ka"
---

BCH (Bose-Chaudhuri-Hocquenghemův kód) je třída výkonných cyklických kódů pro opravu chyb používaných v systémech 3GPP pro dopřednou korekci chyb, která chrání vysílací a řídicí kanály detekcí a opravou bitových chyb.

## Popis

Bose-Chaudhuri-Hocquenghemův (BCH) kód je sofistikovaný blokový kód pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) patřící do rodiny cyklických kódů. Funguje tak, že k původním informačním bitům přidává redundantní paritní bity podle specifické algebraické konstrukce nad konečnými tělesy (Galoisova tělesa). Enkodér generuje kódová slova, kde informační bity a paritní bity splňují sadu polynomiálních rovnic definovaných generujícím polynomem kódu. Tato struktura umožňuje dekodéru detekovat a opravit předem určený počet chyb výpočtem syndromů a řešením poloh chyb pomocí algoritmů, jako je Berlekamp-Masseyho algoritmus a Chienovo prohledávání. Parametry kódu, jako je délka kódového slova (n), počet informačních bitů (k) a schopnost opravy chyb (t), jsou pečlivě vybírány na základě podmínek kanálu a požadované spolehlivosti.

V systémech 3GPP se BCH kódy primárně nasazují k ochraně kritických vysílacích a řídicích informací, které musí být spolehlivě přijaty všemi uživatelskými zařízeními (UE) v buňce. Klíčovou aplikací je transportní kanál Broadcast Channel (BCH), který přenáší Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) obsahující základní systémové informace pro počáteční přístup k buňce. Zpracování na fyzické vrstvě pro transportní kanál BCH zahrnuje kanálové kódování specifickým BCH kódem, následované přizpůsobením rychlosti, scramblováním, modulací a mapováním na fyzické zdroje. Robustnost BCH kódování zajišťuje, že UE mohou úspěšně dekódovat MIB i za špatných podmínek poměru signálu k šumu (SNR), což je zásadní pro výběr buňky, synchronizaci a získání dalších systémových informací.

Implementace a parametry BCH kódů se vyvíjely napříč releasy 3GPP, aby splňovaly požadavky nových technologií rádiového přístupu. V UMTS (3G) se BCH kódování aplikuje na logický kanál Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) mapovaný na transportní kanál BCH. Pro LTE (4G) transportní kanál BCH používá pro MIB konvoluční kód s okusáváním konce (tail-biting), ale BCH kódy se využívají v jiných kontextech, například na Physical Broadcast Channel (PBCH), který nese MIB a používá kombinaci kódovacích schémat. V 5G NR, zatímco PBCH také nese MIB, termín 'BCH' ve specifikacích často odkazuje šířeji na funkčnost vysílacího kanálu a jeho přidruženého řetězce zpracování, který může pro užitečné zatížení zahrnovat polární kódy nebo [LDPC](/mobilnisite/slovnik/ldpc/) kódy, ale konceptuální role robustního kódování vysílacího kanálu zůstává a principy BCH ovlivňují návrh.

## K čemu slouží

BCH kódy byly vytvořeny, aby řešily základní výzvu spolehlivé digitální komunikace přes šumivé a na interference náchylné kanály, jako jsou bezdrátové rádiové spoje. Před sofistikovanou [FEC](/mobilnisite/slovnik/fec/), jako je BCH, komunikační systémy spoléhaly na jednodušší kontroly parity nebo opakovací kódy, které byly neefektivní a nabízely omezenou schopnost opravy chyb. Matematický základ BCH kódů, vyvinutý Boseem, Ray-Chaudhurim a Hocquenghemem, poskytl metodu pro konstrukci kódů s přesně definovanými a výkonnými vlastnostmi pro opravu chyb, což umožnilo systémům udržovat integritu komunikace bez neustálých požadavků na retransmisi, což je pro vysílací provoz neefektivní.

V kontextu mobilních sítí 3GPP je primární motivací pro použití BCH kódování zajistit robustní a spolehlivé doručení kritických systémových vysílacích informací. Kanály jako transportní kanál BCH přenášejí informace zásadní pro vstup do sítě a její provoz, například systémovou šířku pásma a časování rámců. Pokud jsou tyto informace poškozeny, UE se nemůže k síti připojit. BCH kódy to řeší tím, že umožňují UE autonomně opravit určitý počet bitových chyb po přijetí, což výrazně zvyšuje pravděpodobnost úspěšného dekódování na okraji buňky nebo v náročných rádiových podmínkách. Tím se snižuje míra ztráty hovorů a zlepšuje se celková dostupnost a spolehlivost systému.

Přijetí a pokračující odkazování na BCH kódy napříč releasy 3GPP podtrhuje jejich účinnost jako benchmarku pro návrh spolehlivých řídicích kanálů. Zatímco specifická kódovací schémata pro uživatelská data se vyvíjela (např. na Turbo kódy, [LDPC](/mobilnisite/slovnik/ldpc/), polární kódy), požadavky na vysílací kanály konzistentně vyžadovaly vysokou spolehlivost s relativně malými velikostmi bloků, což je oblast, kde BCH kódy vynikají. Jejich použití představuje pečlivý technický kompromis mezi kódovým ziskem, výpočetní složitostí a latencí, což zajišťuje, že vitální řídicí signalizace zůstává robustní, jak se síťové technologie vyvíjejí od 3G přes 5G a dále.

## Klíčové vlastnosti

- Výkonná algebraická oprava chyb schopná opravit více náhodných bitových chyb
- Bloková cyklická struktura kódu umožňující efektivní kódovací a dekódovací algoritmy
- Konfigurovatelné parametry (n, k, t) pro kompromis mezi režií a silou korekce
- Klíčové pro ochranu vysílacích a řídicích kanálů (např. transportní kanál BCH) v systémech 3GPP
- Umožňuje spolehlivé získání systémových informací UE v podmínkách nízkého SNR
- Poskytuje dopřednou korekci chyb, čímž odstraňuje potřebu retransmise na vysílacích kanálech

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [BCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/bch/)
