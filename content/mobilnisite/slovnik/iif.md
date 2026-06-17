---
slug: "iif"
url: "/mobilnisite/slovnik/iif/"
type: "slovnik"
title: "IIF – Internal Interception Function"
date: 2025-01-01
abbr: "IIF"
fullName: "Internal Interception Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iif/"
summary: "Standardizovaná síťová funkce odpovědná za zákonné odposlechy komunikací v rámci sítě 3GPP. Komunikuje s orgány činnými v trestním řízení a poskytuje zachycený obsah a informace související s odposlec"
---

IIF je standardizovaná síťová funkce odpovědná za zákonné odposlechy komunikací v rámci sítě 3GPP, která komunikuje s orgány činnými v trestním řízení a poskytuje zachycený obsah a informace.

## Popis

Internal Interception Function (IIF) je klíčová bezpečnostní a monitorovací komponenta v architektuře sítě 3GPP, definovaná speciálně pro zákonné odposlechy (Lawful Interception, [LI](/mobilnisite/slovnik/li/)). Funguje jako interní entita sítě, která provádí samotný odposlech obsahu komunikace (Content of Communication, [CC](/mobilnisite/slovnik/cc/)) a sbírá informace související s odposlechem (Intercept-Related Information, [IRI](/mobilnisite/slovnik/iri/)) pro konkrétní cíl (např. účastníka nebo IP adresu). IIF je bod, kde je běžný uživatelský provoz a signalizace sítě duplikována a přesměrována pro zákonné účely. Je implementována v různých síťových prvcích, které zpracovávají uživatelská data, jako je Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), Gateway GPRS Support Node (GGSN), Packet Data Network Gateway (PGW), Serving Gateway (SGW), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a uzly IP Multimedia Subsystem (IMS), například Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)).

Provozně je IIF aktivována po obdržení příkazu k zákonnému odposlechu od právně oprávněného subjektu. Tuto aktivaci zprostředkovává Administration Function ([ADMF](/mobilnisite/slovnik/admf/)), další komponenta architektury LI. ADMF odešle požadavek na odposlech, včetně identifikátoru cíle, příslušné IIF v síťovém prvku, který daný cíl obsluhuje. Po aktivaci IIF plní dva hlavní úkoly: generuje Intercept Related Information (IRI), která zahrnuje signalizační data o komunikaci (např. čas sestavení hovoru, zúčastněné strany, poloha), a poskytuje Content of Communication (CC), což je skutečný hlasový, datový nebo zprávový přenos. IIF musí tento odposlech provádět utajeně, aby si cíl sledování neuvědomoval.

IIF přímo nekomunikuje s externími orgány činnými v trestním řízení. Místo toho doručuje zachycená data zprostředkujícím funkcím v doméně síťového operátora. IRI je odeslána do Delivery Function for IRI ([DF2](/mobilnisite/slovnik/df2/)) a CC je odeslána do Delivery Function for CC (DF3). Tyto doručovací funkce pak data bezpečně přeposílají přes standardizovaná rozhraní (HI2 a HI3) do zařízení pro monitorování orgánů činných v trestním řízení (Law Enforcement Monitoring Facility, LEMF). Architektura zajišťuje jasné oddělení mezi interními mechanismy odposlechu sítě (IIF, ADMF, DF) a externí doménou orgánů činných v trestním řízení. Specifikace, zejména 3GPP TS 33.108, podrobně definují předávací rozhraní (HI1, HI2, HI3), datové formáty (např. využití standardů ETSI jako XSD) a protokoly pro tuto komunikaci, aby zajistily interoperabilitu a soulad s právními rámci.

Z pohledu technické implementace zahrnuje IIF hlubokou integraci do logiky řízení hovorů a relací síťových uzlů. Pro přepojované hlasové služby může zachytávat signalizaci řízení hovoru. Pro paketová data zahrnuje duplikaci IP paketů spojených s cílem a jejich zrcadlení do DF3. IIF musí zvládat různé služby: hlasové hovory (CS a VoLTE/VoNR), SMS, MMS a obecné IP datové relace. Její návrh musí také počítat s mobilitou účastníka a zajistit, aby odposlech plynule pokračoval, i když se cíl pohybuje mezi buňkami nebo síťovými oblastmi. Tato funkce je základním kamenem povinnosti síťového operátora poskytovat zákonem požadované odposlechové schopnosti a tvoří komplexní podsystém, který vyvažuje technickou efektivitu, bezpečnost, soukromí pro nezaměřené uživatele a přísné regulatorní požadavky.

## K čemu slouží

Internal Interception Function existuje za účelem plnění zákonných povinností ukládaných poskytovatelům telekomunikačních služeb národními vládami a regulačními orgány. Tyto zákony vyžadují, aby operátoři měli technickou schopnost pomáhat orgánům činným v trestním řízení (LEA) při zákonném odposlechu komunikací pro účely trestního vyšetřování, národní bezpečnosti a zpravodajské činnosti. Před standardizovanými funkcemi, jako je IIF, byly metody odposlechu často proprietární, neškálovatelné a nedokázaly snadno držet krok s vyvíjejícími se síťovými technologiemi, jako je GPRS, 3G a IMS. To vytvářelo problém jak pro operátory, kteří čelili složitým integračním výzvám, tak pro LEA, které potřebovaly konzistentní a spolehlivou metodu pro příjem zachycených dat bez ohledu na podkladovou síťovou technologii nebo zařízení dodavatele.

Vytvoření a standardizace IIF v rámci 3GPP (počínaje Rel-8 jako součást konsolidované architektury LI) tyto problémy vyřešila poskytnutím jednotného rámce nezávislého na dodavateli. Definovala přesně *kde* a *jak* by měl odposlech v architektuře sítě probíhat. Tím se vyřešila omezení ad-hoc řešení zajištěním, že každý kompatibilní síťový prvek (SGSN, GGSN, MME atd.) bude mít konzistentní interní funkci pro generování IRI a CC. Standardizace byla motivována potřebou nákladové efektivity pro operátory (kteří mohou nasazovat sítě více dodavatelů) a provozní efektivity pro LEA, které mohou používat standardizované vybavení pro příjem dat ze sítě libovolného operátora.

Navíc rámec IIF zahrnuje klíčové principy soukromí a bezpečnosti. Přísným definováním interních rozhraní mezi IIF, ADMF a doručovacími funkcemi vytváří auditovatelné a kontrolované prostředí odposlechu v doméně operátora. Tento návrh pomáhá předcházet neoprávněnému přístupu nebo zneužití odposlechových schopností. Také zajišťuje budoucí použitelnost schopnosti, protože základní koncept IIF může být rozšířen na nové síťové funkce v 5G (jako Session Management Function - SMF, User Plane Function - UPF) a nové služby, což zajišťuje, že zákonný odposlech zůstane možný i při vývoji síťových architektur z EPC na 5GC. IIF tedy slouží dvojímu účelu: umožňuje výkon zákonné státní moci a zároveň vynucuje disciplinovanou, standardizovanou a bezpečnou technickou implementaci.

## Klíčové vlastnosti

- Provádí samotný odposlech obsahu (CC) a sběr signalizačních dat (IRI) v síťových uzlech
- Je utajeně aktivována prostřednictvím Administration Function (ADMF) na základě zákonného příkazu
- Je implementována v prvcích jádra sítě (např. MME, SGW, PGW, CSCF)
- Předává zachycená data interním doručovacím funkcím (DF2, DF3)
- Podporuje odposlech napříč více službami (hlas, SMS, paketová data)
- Je navržena pro zvládnutí mobility účastníka a kontinuity relace

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [IIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/iif/)
