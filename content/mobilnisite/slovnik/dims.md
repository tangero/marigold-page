---
slug: "dims"
url: "/mobilnisite/slovnik/dims/"
type: "slovnik"
title: "DIMS – Dynamic and Interactive Multimedia Scene"
date: 2025-01-01
abbr: "DIMS"
fullName: "Dynamic and Interactive Multimedia Scene"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dims/"
summary: "Služba 3GPP umožňující synchronizované, interaktivní multimediální prezentace na více zařízeních. Definuje 'scény' složené z mediálních komponent a scénových příkazů, což umožňuje bohaté, koordinované"
---

DIMS je služba 3GPP umožňující synchronizované, interaktivní multimediální prezentace na více zařízeních definováním scén složených z mediálních komponent a příkazů.

## Popis

DIMS (Dynamic and Interactive Multimedia Scene) je standardizovaná služba 3GPP (TS 26.140), která poskytuje rámec pro vytváření, doručování a vykreslování synchronizovaných, interaktivních multimediálních prezentací. Prezentace DIMS se nazývá 'Scéna'. Scéna je časové uspořádání multimediálních komponent – jako je video, audio, obrázky, text a grafika – které jsou prostorově rozmístěny a mohou se dynamicky měnit na základě uživatelské interakce nebo časovaných událostí. Klíčovou inovací DIMS je 'Scénový příkaz', což je sada instrukcí definovaných ve specifikaci DIMS, které deterministickým způsobem mění stav Scény. Tyto příkazy jsou doručovány spolu s mediálními streamy nebo v jejich rámci.

Z architektonického hlediska služba DIMS zahrnuje několik klíčových entit: DIMS aplikační server, který scénu vytváří a balí; doručovací síť (např. [MBMS](/mobilnisite/slovnik/mbms/), [PSS](/mobilnisite/slovnik/pss/) nebo streamingové servery); a DIMS klient umístěný v uživatelském zařízení. Popis scény, často využívající deklarativní formát, definuje počáteční rozložení, mediální komponenty a jejich vztahy. Dynamické chování je řízeno Scénovými příkazy. Tyto příkazy jsou malé, efektivní instrukce, které mohou spouštět akce jako 'ShowComponent', 'HideComponent', 'MoveTo', 'ChangeVolume' nebo 'LoadNewMedia'. Jsou časově označeny a synchronizovány s časovou osou médií, což zajišťuje, že všichni klienti aktualizují stav Scény přesně ve stejném okamžiku.

DIMS klient je zodpovědný za interpretaci popisu scény, příjem a ukládání do vyrovnávací paměti mediálních komponent a provádění příchozího proudu Scénových příkazů. Udržuje scénový graf reprezentující aktuální stav všech komponent. Po přijetí příkazu klient aktualizuje tento interní model a odpovídajícím způsobem vykreslí změny. To umožňuje komplexní interaktivitu, například umožnění uživateli vybrat si kameru během sportovní události, což spustí Scénový příkaz pro přepnutí zdroje videa, a to vše při zachování synchronizace ostatních grafických prvků na obrazovce. Služba podporuje doručování unicast, multicast a broadcast, což ji činí vhodnou pro personalizované i masmédiové zážitky.

DIMS hraje významnou roli při umožňování multimediálních služeb nové generace. Překračuje rámec jednoduchého streamování a nabízí bohatý, aplikaci podobný zážitek v rámci standardizovaného vysílacího nebo streamovacího rámce. Její synchronizační mechanismy jsou klíčové pro vytváření 'společných sledovacích' zážitků, kde více uživatelů současně vidí stejné interaktivní prvky. Navíc oddělením řídicí logiky (Scénové příkazy) od mediálních dat umožňuje lehké aktualizace a personalizaci bez nutnosti znovuvysílání celých video streamů, čímž optimalizuje využití šířky pásma.

## K čemu slouží

DIMS byl vytvořen, aby řešil omezení tradičních lineárních vysílacích a služeb streamování na vyžádání, které nabízely malý prostor pro synchronizovanou interaktivitu a víceobrazovkové zážitky. Před DIMS vyžadovalo vytvoření interaktivní televizní zkušenosti, kde by se grafika, alternativní audio stopy nebo kamery mohly synchronizovaně měnit napříč miliony diváků, proprietární, neinteroperabilní technologie. To fragmentovalo trh a zvyšovalo náklady pro tvůrce obsahu a výrobce zařízení.

Primární problém, který DIMS řeší, je standardizované doručování synchronizovaných, stavových multimediálních prezentací. Byl motivován rostoucí poptávkou po obohacené televizi (např. sportovní statistiky v překryvu, interaktivní reklama, příběhy typu 'zvol si svou vlastní cestu') a rozšířením aplikací pro druhou obrazovku. Bez DIMS byla synchronizace doprovodné aplikace na tabletu s hlavním vysíláním na televizoru složitá a náchylná k chybám. DIMS poskytuje jednotný model, kde jediná vytvořená Scéna může být konzistentně vykreslena na různých typech zařízení s vestavěnými mechanismy pro uživatelský vstup a změny stavu.

Historicky byl DIMS (zavedený ve vydání 8) součástí širšího úsilí 3GPP o pokročilé multimediální služby spolu s [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) a [PSS](/mobilnisite/slovnik/pss/) (Packet Switched Streaming). Cílem bylo využít obousměrné schopnosti mobilních sítí k přidání interaktivity k vysílanému obsahu. Tato technologie byla také považována za umožňující faktor pro bohatá mediální vzdělávání, interaktivní reklamu a vylepšené systémy varování veřejnosti. Poskytnutím standardizovaného modelu 'scénového grafu' a sady příkazů umožnil tvůrcům obsahu psát jednou a nasazovat všude, což podporovalo inovace v interaktivních médiích a zároveň zajišťovalo spolehlivost a synchronizaci – klíčové aspekty, kde předchozí ad-hoc řešení selhávala.

## Klíčové vlastnosti

- Definuje 'Scénové příkazy' jako standardizovanou sadu instrukcí pro dynamickou modifikaci multimediální prezentace.
- Podporuje přesnou časovou synchronizaci příkazů s přehráváním médií na více zařízeních.
- Umožňuje bohatou interaktivitu, což umožňuje, aby uživatelské vstupy spouštěly změny stavu scény.
- Používá deklarativní formát popisu scény k definování počátečního rozložení a mediálních komponent.
- Podporuje více doručovacích mechanismů včetně unicast (PSS), broadcast/multicast (MBMS) a stahování souborů.
- Umožňuje víceobrazovkové a synchronizované zážitky s druhou obrazovkou z jediné vytvořené scény.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.430** (Rel-19) — Timed Graphics Media Type Specification
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study

---

📖 **Anglický originál a plná specifikace:** [DIMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dims/)
