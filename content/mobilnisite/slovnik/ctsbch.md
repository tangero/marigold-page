---
slug: "ctsbch"
url: "/mobilnisite/slovnik/ctsbch/"
type: "slovnik"
title: "CTSBCH – CTS Beacon Channel"
date: 2025-01-01
abbr: "CTSBCH"
fullName: "CTS Beacon Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctsbch/"
summary: "CTS Beacon Channel je vyhrazený vysílací kanál používaný v sítích GSM pro podporu funkce CTS (Cordless Telephony System), známé také jako propojení GSM-WLAN. Poskytuje majákové signály, které umožňují"
---

CTSBCH je vyhrazený vysílací kanál v sítích GSM, který poskytuje majákové signály pro dvou režimové terminály, aby mohly objevit a synchronizovat se s přístupovými body systému Cordless Telephony System.

## Popis

[CTS](/mobilnisite/slovnik/cts/) Beacon Channel (CTSBCH) je klíčová komponenta definovaná ve specifikaci 3GPP TS 43.052 pro funkci Cordless Telephony System (CTS), která umožňuje propojení GSM-WLAN. Funguje jako vyhrazený vysílací kanál vysílaný přístupovými body CTS (CTS-AP) v neregulovaném kmitočtovém spektru, typicky v pásmech 2,4 GHz nebo 5 GHz. Primární funkcí CTSBCH je vysílat základní systémové informace a synchronizační signály, které umožňují dvou režimovému uživatelskému zařízení (UE) GSM/CTS detekovat, identifikovat a připojit se k buňce CTS. Kanál nese specifickou strukturu majákového rámce obsahující parametry nezbytné pro počáteční přístup, včetně identity systému CTS, časových informací a konfiguračních údajů pro přidružené kanály pro přenos a řízení.

Z architektonického hlediska je CTSBCH součástí rozhraní mezi CTS-AP a UE. CTS-AP, které se připojuje k jádru sítě GSM přes standardní rozhraní A nebo Gb, periodicky vysílá CTSBCH, aby oznámilo svou přítomnost a schopnosti. Vysílání majáku sleduje definovaný vzor a úroveň výkonu, aby byla zajištěna spolehlivá detekce a zároveň minimalizován vliv na jiné systémy v neregulovaných pásmech. Struktura kanálu zahrnuje synchronizační sekvence, bloky systémových informací a volitelná rozšiřující pole, která mohou nést další konfigurační parametry. Rámce majáku jsou vysílány v pravidelných intervalech, typicky každých několik set milisekund, aby byl vyvážen rychlý objev a energetická účinnost pro [AP](/mobilnisite/slovnik/ap/) i hledající UE.

Z procesního pohledu, když dvou režimové UE vstoupí do oblasti pokrytí CTS nebo je nakonfigurováno k hledání služby CTS, prohledává určená neregulovaná kmitočtová pásma pro signály CTSBCH. Po detekci platného majáku dekóduje UE systémové informace, aby získalo potřebné parametry pro registraci a následnou komunikaci. To zahrnuje identitu oblasti umístění CTS (CTS-LAI), podporované služby, parametry řízení přístupu a informace o časové synchronizaci. UE používá tyto informace k synchronizaci s časovou strukturou CTS-AP a zahájení registrační procedury přes přidružený náhodný přístupový kanál (CTS-RACH) a kanál pro udělení přístupu (CTS-AGCH). CTSBCH v podstatě plní funkce analogické kanálu [BCCH](/mobilnisite/slovnik/bcch/) (Broadcast Control Channel) v konvenčních buňkách GSM, ale je optimalizován pro prostředí neregulovaných pásem a specifické požadavky CTS.

Technická implementace CTSBCH zahrnuje specifické modulační schémata, kódovací rychlosti a struktury rámců definované tak, aby zajistily robustní provoz v potenciálně rušených neregulovaných pásmech. Kanál používá modulaci [GMSK](/mobilnisite/slovnik/gmsk/) (Gaussian Minimum Shift Keying) podobnou standardnímu GSM, ale s úpravami pro odlišné kmitočtové charakteristiky. Mechanizmy ochrany proti chybám zahrnují konvoluční kódování a kontrolní součty cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)), aby bylo zajištěno spolehlivé přijetí kritických systémových informací. Výkon vysílání majáku a pracovní cyklus jsou pečlivě řízeny, aby vyhovovaly regulatorním požadavkům pro provoz v neregulovaných pásmech, a zároveň byla zachována přiměřená oblast pokrytí. Kanál také podporuje mechanismy pro vyrovnávání zatížení a převýběr buňky vysíláním parametrů, které pomáhají UE učinit inteligentní rozhodnutí o tom, který CTS-AP vybrat na základě kvality signálu, dostupné kapacity a schopností služeb.

V širším kontextu sítě CTSBCH umožňuje dvou režimový provoz, který tvoří základ propojení GSM-WLAN. Umožňuje mobilním operátorům rozšířit pokrytí svých služeb do vnitřních prostorů pomocí nízkonákladových přístupových bodů CTS při zachování plynulé kontinuity služeb. Návrh kanálu zajišťuje, že terminály s podporou CTS mohou efektivně objevovat dostupné pokrytí CTS, autentizovat se v síti a předávat hovory mezi makro buňkami GSM a vnitřními buňkami CTS s minimálním přerušením služby. Tato schopnost byla zvláště cenná v době, kdy byl CTS vyvíjen, neboť poskytovala ranou konvergenci mezi buněčnými a WLAN technologiemi a připravovala cestu pro pozdější jednotné komunikační systémy.

## K čemu slouží

[CTS](/mobilnisite/slovnik/cts/) Beacon Channel byl vytvořen, aby řešil rostoucí poptávku po lepším vnitřním pokrytí a kapacitě v sítích GSM na konci 90. let a začátkem 21. století. Tradiční makro buňky GSM často nedokázaly poskytnout spolehlivou službu uvnitř budov kvůli útlumu signálu stěnami a dalšími překážkami. Přestože existovala specializovaná vnitřní řešení jako pikobuňky a opakovače, jejich nasazení a provoz byly nákladné. Koncept Cordless Telephony System (CTS) se objevil jako nákladově efektivní alternativa, která využívala neregulovaná kmitočtová pásma a zjednodušený hardware přístupových bodů k vytvoření rozšíření vnitřního pokrytí. CTSBCH byl konkrétně navržen, aby umožnil tuto architekturu tím, že poskytuje potřebný majákový mechanismus pro objev a synchronizaci terminálů v prostředí neregulovaných pásem.

Primární problém, který CTSBCH řeší, je efektivní objev a výběr přístupových bodů CTS dvou režimovými terminály. Bez standardizovaného majákového kanálu by každý výrobce mohl implementovat proprietární mechanismy objevu, což by vedlo k problémům s interoperabilitou a roztříštěným přijetím na trhu. CTSBCH poskytuje jednotnou metodu, jak mohou CTS-AP oznamovat svou přítomnost a schopnosti, a zajišťuje, že jakýkoli kompatibilní dvou režimový terminál může objevit a připojit se k jakémukoli kompatibilnímu CTS-AP. Tato standardizace byla klíčová pro vytvoření životaschopného ekosystému interoperabilního zařízení od více výrobců. CTSBCH navíc řeší technické výzvy provozu v neregulovaných pásmech, včetně správy rušení, dodržování regulatorních požadavků a energeticky efektivních procedur objevu.

Historicky CTS a jeho komponenta CTSBCH představovaly důležitý krok v konvergenci buněčných a bezšňůrových/WLAN technologií. Umožnily mobilním operátorům využít existující zařízení na straně zákazníka (jako jsou domácí širokopásmová připojení) k rozšíření pokrytí jejich sítě bez nutnosti nákladného licencovaného spektra nebo složité infrastruktury. Technologie řešila omezení předchozích přístupů, jako byly samostatné bezšňůrové systémy ([DECT](/mobilnisite/slovnik/dect/)), které se nemohly plynule integrovat s buněčnými sítěmi, nebo raná proprietární řešení bez interoperability. Přestože samotný CTS zaznamenal ve srovnání s pozdějšími technologiemi, jako jsou UMA/[GAN](/mobilnisite/slovnik/gan/) a VoWiFi, omezené komerční nasazení, koncepty a mechanismy vyvinuté pro CTSBCH ovlivnily následné standardizační úsilí pro propojení buněčných sítí a WLAN a pomohly stanovit základní principy pro konvergenci více přístupových sítí.

## Klíčové vlastnosti

- Standardizované vysílání majáku v neregulovaných kmitočtových pásmech (2,4 GHz/5 GHz)
- Nese základní systémové informace včetně identity CTS a konfiguračních parametrů
- Podporuje synchronizaci a časové sladění pro dvou režimové terminály
- Umožňuje efektivní mechanismy objevu a výběru buňky
- Poskytuje ochranu proti chybám prostřednictvím konvolučního kódování a CRC
- Usnadňuje plynulou mobilitu mezi makro buňkami GSM a vnitřním pokrytím CTS

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [CTSBCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctsbch/)
