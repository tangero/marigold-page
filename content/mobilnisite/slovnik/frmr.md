---
slug: "frmr"
url: "/mobilnisite/slovnik/frmr/"
type: "slovnik"
title: "FRMR – Frame Reject"
date: 2025-01-01
abbr: "FRMR"
fullName: "Frame Reject"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/frmr/"
summary: "Typ řídicího rámce ve vrstvě datového spoje GSM (protokol LAPDm) používaný k nahlášení neopravitelných chyb v přijatém rámci. Iniciuje procedury opakovaného přenosu a zajišťuje integritu dat přes rádi"
---

FRMR je řídicí rámec GSM LAPDm používaný k nahlášení neopravitelných chyb v přijatém rámci, který iniciuje opakovaný přenos pro zajištění integrity dat přes rádiové rozhraní.

## Popis

Frame Reject (FRMR) je specifický supervízorový rámec definovaný v protokolu Link Access Protocol on the Dm channel (LAPDm), což je protokol vrstvy datového spoje (vrstva 2) používaný pro signalizaci a přenos dat na rádiovém rozhraní v GSM (a jeho evoluci). LAPDm je adaptací protokolu [ISDN](/mobilnisite/slovnik/isdn/) [LAPD](/mobilnisite/slovnik/lapd/) pro specifická omezení mobilní rádiové cesty. Rámec FRMR je klíčovým mechanismem pro obnovu při chybě, když dojde k porušení protokolu, které nelze opravit standardní chybou kontrolního součtu ([CRC](/mobilnisite/slovnik/crc/)) nebo chybami čísel sekvencí řešenými rámci REJ (Reject).

FRMR funguje následovně: Když přijímač (mobilní stanice/[MS](/mobilnisite/slovnik/ms/) nebo základnová stanice/[BSS](/mobilnisite/slovnik/bss/)) přijme rámec, který je syntakticky správný (projde kontrolou Frame Check Sequence), ale obsahuje chybu protokolu, odešle vysílači rámec FRMR. Mezi chyby protokolu patří přijetí nedefinovaného nebo neimplementovaného typu rámce, rámce s informačním polem delším, než je maximální povolená délka, nebo s neplatným parametrem řídicího pole (např. bit poll/final nastavený nesprávně v daném kontextu). Samotný rámec FRMR obsahuje informační pole, které zahrnuje kopii řídicího pole zamítnutého rámce a často také diagnostický kód vysvětlující konkrétní důvod zamítnutí. To umožňuje vysílající straně diagnostikovat přesný nesoulad v protokolu.

Po přijetí FRMR musí vysílač provést specifické akce pro obnovu definované stavovým automatem LAPDm. Typicky to zahrnuje reset spojení vrstvy datového spoje pro daný logický kanál. To může znamenat opětovné navázání spojení, což zajistí, že si oba konce znovu synchronizují své stavové proměnné (vysílací a přijímací čísla sekvencí, V(S) a V(R)). Mechanismus FRMR je nouzovou procedurou pro zpracování chyb, neboť signalizuje narušení dohodnuté činnosti protokolu mezi dvěma protistranami. Je klíčový pro udržení integrity a konzistence signalizačních zpráv (např. pro řízení hovorů, správu mobility) a paketů uživatelských dat (v [GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/)) přes nespolehlivé rádiové spojení a zajišťuje, že přetrvávající chyby protokolu nezpůsobí tiché selhání nebo nedefinované chování.

## K čemu slouží

Mechanismus Frame Reject existuje pro zpracování specifické třídy chyb v komunikaci na vrstvě datového spoje: porušení protokolu. V jakémkoli spolehlivém protokolu datového spoje jsou jednoduché bitové chyby detekovány pomocí Frame Check Sequence ([FCS](/mobilnisite/slovnik/fcs/)/CRC) a rámce s chybou CRC jsou tiše zahozeny, přičemž se spoléhá na časovače a čísla sekvencí vyšších vrstev (jako v rámcích REJ), aby spustily opakovaný přenos. Některé chyby však vedou k rámci, který je technicky platný podle FCS, ale logicky neplatný podle stavového automatu nebo pravidel protokolu.

Bez FRMR by takové rámce s chybou protokolu mohly způsobit, že obě komunikující strany přestanou být synchronizované nebo přejdou do nedefinovaného stavu. Například pokud jedna strana začne vysílat nový, delší typ informačního rámce, kterému software druhé strany nerozumí, přijímač by jej mohl jednoduše zahodit. Vysílač by jej při nedostání potvrzení mohl donekonečna opakovat, což by způsobilo deadlock. Rámec FRMR poskytuje formální mechanismus přímého oznámení v rámci přenosu k rozrušení tohoto deadlocku. Informuje odesílatele: 'Přijal jsem váš rámec, prošel kontrolou CRC, ale nemohu jej zpracovat kvůli porušení pravidla protokolu; potřebujeme resetovat naši konverzaci.'

Tato schopnost byla obzvláště důležitá při návrhu LAPDm pro GSM, který musel být robustní pro provoz v náročném, na chyby náchylném rádiovém kanálu a zároveň podporovat více logických kanálů (SDCCH, SACCH, FACCH) pro kritickou síťovou signalizaci. Zajišťuje, že jakákoli zásadní nekompatibilita nebo softwarová chyba způsobující nesprávné použití protokolu může být detekována a procedura obnovy (reset spoje) může být automaticky zahájena, čímž se udržuje celková stabilita systému a zabrání se uváznutí hovorů v neobnovitelném stavu signalizační chyby. Tento princip použití FRMR (nebo jeho ekvivalentu, jako je FRMR v LAPD) je klasický koncept z oblasti datových komunikací přizpůsobený pro mobilní prostředí.

## Klíčové vlastnosti

- Supervízorový typ rámce LAPDm pro hlášení neobnovitelných chyb protokolu
- Obsahuje diagnostické pole s řídicím polem zamítnutého rámce a příčinou chyby
- Spouští proceduru resetu vrstvy datového spoje pro opětovnou synchronizaci komunikujících stran
- Zpracovává chyby jako nedefinované typy rámců nebo neplatné parametry řídicího pole
- Funguje na rozhraní Um mezi MS a BSS pro GSM signalizaci a data
- Nouzový mechanismus obnovy při chybě, když standardní ARQ selže

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [FRMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/frmr/)
