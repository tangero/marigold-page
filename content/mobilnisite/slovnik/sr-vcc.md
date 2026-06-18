---
slug: "sr-vcc"
url: "/mobilnisite/slovnik/sr-vcc/"
type: "slovnik"
title: "SR-VCC – Single Radio Voice Call Continuity"
date: 2025-01-01
abbr: "SR-VCC"
fullName: "Single Radio Voice Call Continuity"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sr-vcc/"
summary: "SR-VCC je standard 3GPP pro plynulé předání hlasového hovoru z paketově orientované sítě LTE/5G (pomocí VoLTE nebo VoNR) do starší okruhově orientované sítě 2G/3G. Zajišťuje kontinuitu hlasové služby,"
---

SR-VCC je standard 3GPP pro plynulý předání hovoru z paketově orientované sítě LTE/5G do starší okruhově orientované sítě 2G/3G, který umožňuje zachovat hovor bez přerušení při změně pokrytí.

## Popis

Single Radio Voice Call Continuity (SR-VCC) je funkce mobility a kontinuity služeb definovaná pro koncová zařízení s jedním rádiovým transceiverem. Jejím hlavním účelem je řídit předávání probíhajícího hlasového hovoru z hlasové služby založené na IP Multimedia Subsystem (IMS) (jako Voice over LTE – VoLTE) v paketově orientované ([PS](/mobilnisite/slovnik/ps/)) doméně na okruhově orientovanou ([CS](/mobilnisite/slovnik/cs/)) hlasovou službu v síti 2G ([GERAN](/mobilnisite/slovnik/geran/)) nebo 3G ([UTRAN](/mobilnisite/slovnik/utran/)). Architektura zahrnuje úzkou interakci mezi Evolved Packet Core (EPC), jádrem IMS a starším okruhově orientovaným jádrem sítě ([MSC](/mobilnisite/slovnik/msc/)). Mezi klíčové síťové prvky patří [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity), MSC Server rozšířený o funkcionalitu rozhraní Sv (známý jako MSC Server enhanced for SR-VCC) a aplikační server IMS (např. Service Centralization and Continuity Application Server – [SCC](/mobilnisite/slovnik/scc/) [AS](/mobilnisite/slovnik/as/)).

Procedura SR-VCC je iniciována sítí a je spuštěna na základě měřicích hlášení od uživatelského zařízení (UE). Když se UE účastnící se hovoru VoLTE pohybuje na okraj pokrytí LTE, odešle měřicí hlášení indikující silnější signály 2G/3G. Stanice LTE (eNodeB) toto hlášení přepošle MME. MME, které rozpozná hlasový přenos, zahájí proceduru SR-VCC odesláním žádosti o předání přes rozhraní Sv na MSC Server. MSC Server následně koordinuje s cílovou rádiovou sítí 2G/3G a okruhově orientovaným jádrem sítě, aby připravil prostředky. Zásadní je, že MSC Server také komunikuje s aplikačním serverem SCC v IMS, aby provedl přenos relace a ukotvil větev hovoru od protistrany v CS síti. Z pohledu UE obdrží příkaz k předání z LTE do buňky 2G/3G a jeho jediný radiový transceiver se přeladí na novou frekvenci, kde je okruhově orientovaný hlasový hovor již navázán.

Úlohou SR-VCC je fungovat jako klíčový mechanismus interoperability a záložního řešení během přechodného období, kdy nebylo pokrytí LTE všudypřítomné. Chrání uživatelský zážitek z hlasových služeb, které jsou považovány za kritické, tím, že využívá rozsáhlé pokrytí starších CS sítí. Procedura zvládá nejen přenos rádiového přístupu, ale také plynulý přenos řízení hovoru a mediální cesty na aplikační vrstvě IMS, čímž zajišťuje, že hovor není přerušen. Specifikace jako TS 23.216 a TS 24.237 poskytují podrobnosti protokolů fáze 2 a fáze 3 pro toto předávání mezi systémy.

## K čemu slouží

SR-VCC bylo vytvořeno k řešení specifického problémů nasazení sítí LTE: jak zajistit spolehlivou a všudypřítomnou hlasovou službu již od počátku, přestože LTE bylo navrženo jako čistě IP, pouze paketová síť bez nativní okruhově orientované hlasové domény. V raných nasazeních LTE bylo pokrytí omezeno na městské oblasti, zatímco sítě 2G a 3G poskytovaly téměř celostátní pokrytí pro hlas. Bez SR-VCC by se hovor VoLTE při opuštění pokrytí LTE prostě přerušil, což by vedlo ke špatnému uživatelskému zážitku a znemožnilo by komerční využití VoLTE jako primární hlasové služby.

Historický kontext představuje přechod od okruhově orientovaného hlasu v sítích 2G/3G k IP hlasu (VoIP) v sítích 4G. Operátoři potřebovali řešení, které by jim umožnilo spustit LTE pro vysokorychlostní data, a přitom se pro pokrytí hlasem mohli opírat o stávající CS síť, s hladkou cestou k postupnému přechodu hlasu na VoLTE. SR-VCC tento most poskytlo. Řešilo omezení dřívějších řešení kontinuity hlasu, jako bylo VCC (definované pro 3G), která byla navržena pro zařízení s dvojím rádiem a neefektivně zvládala omezení jediného rádiového transceiveru moderních smartphonů.

Účelem SR-VCC bylo umožnit komerční spuštění hlasu přes LTE založeného na IMS tím, že garantovalo kontinuitu, a tím urychlit adopci LTE pro data i hlas. Poskytlo operátorům důvěru k nasazení VoLTE s vědomím, že mohou využít svou starší síť jako záložní řešení. Šlo o klíčový krok ve vývoji směrem k čistě IP sítím a v konečném důsledku to pomohlo připravit cestu pro čisté pokrytí VoLTE/VoNR, jak se sítě LTE rozšiřovaly, a pro postupné vyřazování starších CS sítí.

## Klíčové vlastnosti

- Plynulé předání hlasových hovorů IMS z paketové domény LTE do okruhové domény 2G/3G
- Navrženo pro uživatelská zařízení s jedním rádiovým transceiverem
- Zahrnuje koordinaci mezi MME, MSC Serverem a aplikačním serverem SCC v IMS
- Využívá rozhraní Sv mezi MME a MSC
- Zachovává kontinuitu hlasového hovoru při mobilitě mezi různými rádiovými přístupovými technologiemi (inter-RAT)
- Kritické pro raná nasazení VoLTE a rozšíření pokrytí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [SR-VCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sr-vcc/)
