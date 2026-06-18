---
slug: "csaf"
url: "/mobilnisite/slovnik/csaf/"
type: "slovnik"
title: "CSAF – CS Adaptation Function"
date: 2007-01-01
abbr: "CSAF"
fullName: "CS Adaptation Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csaf/"
summary: "CS Adaptation Function (CSAF) je funkční entita zavedená ve specifikaci 3GPP Release 7, která umožňuje poskytování služeb domény přepojování okruhů (Circuit-Switched, CS) přes IP transportní sítě, kon"
---

CSAF je funkční entita, která adaptuje služby přepojování okruhů (Circuit-Switched) pro přenos přes IP sítě, což umožňuje provoz zastaralých služeb, jako jsou hlasová volání, v rámci IP Multimedia Subsystem (IMS).

## Popis

[CS](/mobilnisite/slovnik/cs/) Adaptation Function (CSAF) je prvek jádra sítě definovaný v rámci architektury 3GPP pro služby založené na IP Multimedia Subsystem (IMS). Jeho primární technickou rolí je poskytnout potřebnou adaptační vrstvu mezi zastaralou doménou jádra sítě s přepojováním okruhů (Circuit-Switched, CS) a paketově orientovaným IMS. Z architektonického hlediska je CSAF pozicována jako zprostředkující funkce. Na jedné straně komunikuje se sítí CS, typicky se připojuje k ústřednám mobilní sítě (Mobile Switching Centers, MSCs) pomocí standardních protokolů CS, jako jsou [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) nebo BICC (Bearer Independent Call Control). Na druhé straně komunikuje s jádrem IMS, konkrétně s funkcí Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a IMS Media Gateway ([IMS-MGW](/mobilnisite/slovnik/ims-mgw/)), přičemž používá protokol [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) pro řízení hovorů a [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) pro přenos médií přes IP.

Z funkční perspektivy CSAF funguje tak, že provádí převod protokolů a adaptaci médií. Pro signalizaci překládá mezi signalizací pro řízení hovorů specifickou pro CS (např. zprávy ISUP) a jejich ekvivalenty v SIP používanými v IMS. To zahrnuje mapování informací o sestavování a ukončování hovorů a doplňkových služeb mezi oběma doménami. Pro uživatelskou rovinu (přenos datových toků) CSAF spravuje adaptaci mediálního proudu. Zajišťuje vzájemnou spolupráci mezi 64 kbps PCM (Pulse-Code Modulation) hlasovými kanály používanými v doméně CS a paketizovanými hlasovými kodeky (jako AMR) přenášenými přes RTP/IP v doméně IMS. To často zahrnuje, že CSAF řídí přidružený prostředek mediální brány (media gateway), aby provedl skutečný převod kodeku nebo průchod médií.

Klíčovou součástí fungování CSAF je její role v architektuře IMS Service Centralization and Continuity (SCC), která byla hlavním motivem pro její specifikaci. V tomto kontextu CSAF umožňuje ukotvení (anchoring) CS hovorů v IMS. Když uživatelské zařízení (User Equipment, UE) iniciuje nebo přijímá CS hovor, CSAF umožňuje IMS převzít kontrolu nad touto relací. Tato centralizace v IMS je klíčová pro umožnění pokročilých funkcí kontinuity služeb, jako je Voice Call Continuity (VCC) a později Single Radio Voice Call Continuity (SRVCC), kdy může být probíhající hlasový hovor plynule předán mezi doménou CS a doménou IMS/PS.

Implementace CSAF je kritická pro postupnou evoluci sítě. Umožňuje operátorům mobilních sítí zavádět a rozšiřovat svou IMS infrastrukturu pro hlasové a multimediální služby, zatímco jejich zastaralá síť CS zůstává v provozu a obsluhuje účastníky, kteří ještě nejsou IMS-kompatibilní nebo se nacházejí v oblastech bez pokrytí IMS. Ukotvováním relací pocházejících z CS v IMS mohou operátoři začít nasazovat nové, IP-based služby, které jsou dostupné i uživatelům v zastaralé síti, čímž vytvářejí jednotnou služební vrstvu. Technicky odděluje služební logiku (v IMS) od přístupové technologie a připravuje cestu pro případné vyřazení tradičního jádra sítě CS.

## K čemu slouží

CSAF byla vytvořena, aby vyřešila zásadní výzvu při přechodu z tradičních mobilních sítí s přepojováním okruhů na plně IP sítě založené na IMS. Před zavedením IMS byly všechny hlasové služby a služby SMS poskytovány výhradně prostřednictvím jádra sítě s přepojováním okruhů (Circuit-Switched, CS) (MSC/VLR). Zavedení IMS v Release 5 nabídlo novou, IP-based platformu pro poskytování multimediálních služeb, ale vytvořilo paralelní služební izolovaný systém. Bez mostu nemohli účastníci v síti CS přistupovat ke službám IMS a účastníci IMS nemohli vzájemně komunikovat s obrovskou instalovanou základnou uživatelů CS. Toto rozdělení bránilo adopci IMS a zabraňovalo operátorům v konsolidaci jejich služebních platforem.

Primární problém, který CSAF řeší, je interoperabilita služeb a evoluce sítě. Umožňuje poskytování toho, co se jeví jako tradiční služby CS (jako jsou hlasová volání), ale které jsou ve skutečnosti směrovány a řízeny přes IMS. To umožňuje síťovým operátorům začít migrovat služební logiku a inteligenci na moderní, flexibilní platformu IMS, a přitom nadále využívat svou stávající infrastrukturu sítě CS pro přístup a přenos tam, kde je to potřeba. Byl to klíčový prvek pro koncept 'Service Centralization', kde se IMS stává centrálním bodem pro řízení služeb bez ohledu na podkladovou přístupovou síť (CS nebo PS).

Historicky byl její vývoj v Release 7 motivován potřebou konkrétních mechanismů pro podporu hlasových služeb založených na IMS a především kontinuity služeb. Koncepty jako Voice Call Continuity (VCC) vyžadovaly bod vzájemného propojení, kde by mohla být relace hovoru ukotvena a následně převedena mezi doménami. CSAF poskytuje tento ukotvovací bod pro hovory z legacy sítě CS. Vyřešila omezení spočívající ve dvou oddělených, nekompatibilních služebních jádrech tím, že fungovala jako brána a adaptační vrstva, díky čemuž se IMS stalo sjednocující služební vrstvou pro přístupy jak s přepojováním paketů, tak s přepojováním okruhů. To byl zásadní krok k dlouhodobému cíli jednotného, konsolidovaného jádra sítě založeného na IP.

## Klíčové vlastnosti

- Vzájemná spolupráce protokolů (Interworking) mezi signalizací CS (ISUP/BICC) a IMS (SIP)
- Adaptace médií pro provoz v uživatelské rovině mezi formáty TDM/PCM a RTP/IP
- Ukotvení hovorů (Call Anchoring) v IMS pro relace pocházející z domény CS
- Podpora architektury IMS Service Centralization and Continuity (SCC)
- Umožňuje funkce Voice Call Continuity (VCC) a Single Radio VCC (SRVCC)
- Usnadňuje postupnou migraci sítě z CS na plně IP jádro IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS-MGW – IP Multimedia Subsystem Media Gateway Function](/mobilnisite/slovnik/ims-mgw/)

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS

---

📖 **Anglický originál a plná specifikace:** [CSAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/csaf/)
