---
slug: "gsk"
url: "/mobilnisite/slovnik/gsk/"
type: "slovnik"
title: "GSK – Group Session Key"
date: 2025-01-01
abbr: "GSK"
fullName: "Group Session Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gsk/"
summary: "Kryptografický klíč používaný k zabezpečení skupinové komunikace v sítích 3GPP. Umožňuje efektivní a bezpečnou distribuci obsahu nebo dat k více zařízením současně, například u služeb MBMS nebo MCPTT."
---

GSK je kryptografický klíč používaný k zabezpečení skupinové komunikace, jako jsou služby MBMS nebo MCPTT, který chrání vysílací a multicastový provoz před odposlechem a neoprávněnou manipulací.

## Popis

Skupinový relací klíč (GSK) je bezpečnostní klíč definovaný v architektuře 3GPP, konkrétně pro skupinově orientované služby. Jedná se o symetrický klíč používaný k šifrování a zajištění integrity dat odesílaných ze síťové entity (jako je [BM-SC](/mobilnisite/slovnik/bm-sc/) v [MBMS](/mobilnisite/slovnik/mbms/)) ke skupině uživatelských zařízení (UE). GSK není jedinečný pro každé UE; místo toho je stejný klíč sdílen mezi všemi autorizovanými členy konkrétní služební skupiny, což umožňuje efektivní zabezpečení vysílání/multicastu. Životní cyklus klíče – generování, distribuce, používání a zrušení – je řízen klíčovými manažerskými entitami sítě.

Z architektonického hlediska je GSK typicky generován funkcí pro správu klíčů (KMF) nebo klíčovým manažerským systémem poskytovatele služeb. V kontextu služby Multimedia Broadcast Multicast Service (MBMS) je GSK často spojován s hierarchií klíče služby MBMS ([MSK](/mobilnisite/slovnik/msk/)). GSK je odvozen z klíče vyšší úrovně, jako je uživatelský klíč MBMS ([MUK](/mobilnisite/slovnik/muk/)), nebo distribuován za jeho použití, případně za použití služebně specifického klíče, čímž je zajištěno, že pouze UE s příslušnými přihlašovacími údaji mohou získat přístup ke skupinovému klíči. Klíč je následně použit k zašifrování provozního klíče (TK), který následně šifruje vlastní mediální obsah, čímž vzniká vrstvený bezpečnostní model.

Při provozu je GSK distribuován k UE prostřednictvím zabezpečených unicastových kanálů (např. za použití individuálního bezpečnostního kontextu každého UE) před zahájením skupinové relace. Jakmile všechna autorizovaná UE vlastní GSK, může síť vysílat šifrovaný obsah pomocí šifrovacího klíče odvozeného z GSK. Tento mechanismus se vyhýbá nutnosti šifrovat provoz individuálně pro každé UE, což by bylo pro velké skupiny neúměrně náročné na zdroje. GSK může být periodicky aktualizován nebo může dojít k jeho výměně (rekeying) za účelem udržení bezpečnosti, zejména při změně členství ve skupině nebo pro prevenci kompromitace klíče v čase.

GSK hraje klíčovou roli při umožnění bezpečných skupinových komunikačních služeb definovaných 3GPP, jako je MBMS pro vysílání videa, Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) pro veřejnou bezpečnost a potenciálně skupinové zprávy pro IoT. Jeho existence umožňuje operátorům nabízet škálovatelné, bezpečné multicastové služby bez obětování bezpečnosti jednotlivých uživatelů. Specifikace upravující GSK, především TS 33.303, podrobně popisují funkce odvozování klíčů, distribuční protokoly a integraci s celkovými rámci pro autentizaci a dohodu o klíči 3GPP.

## K čemu slouží

Skupinový relací klíč byl zaveden, aby řešil základní bezpečnostní výzvu efektivního zabezpečení dat odesílaných více příjemcům v mobilní síti. Tradiční unicastové zabezpečení, kde má každé UE jedinečný klíč, není pro vysílací nebo multicastové scénáře škálovatelné, protože šifrování stejného obsahu různými klíči pro tisíce uživatelů plýtvá přenosovou kapacitou a výpočetním výkonem. GSK poskytuje sdílené tajemství pro definovanou skupinu, což umožňuje, aby jeden šifrovaný proud byl dešifrován všemi autorizovanými členy skupiny.

Historicky, jak 3GPP vyvíjelo skupinově orientované služby jako [MBMS](/mobilnisite/slovnik/mbms/), stala se zřejmou potřeba standardizovaného skupinového bezpečnostního mechanismu. Rané systémy pro vysílání multimédií postrádaly robustní, standardizované zabezpečení, což riskovalo neoprávněný přístup k prémiovému obsahu nebo citlivé skupinové komunikaci. Rámec GSK, zavedený ve vydání 12, poskytl strukturovanou hierarchii klíčů v rámci stávající bezpečnostní architektury 3GPP (EPS nebo 5GS), čímž zajistil zpětnou kompatibilitu a integraci s existujícími procedurami pro autentizaci a dohodu o klíči ([AKA](/mobilnisite/slovnik/aka/)).

Řeší problém bezpečné a efektivní správy klíčů pro služby hromadného doručování. Bez mechanismu typu GSK by museli operátoři buď akceptovat nezabezpečené vysílání, nebo implementovat proprietární, vzájemně nekompatibilní řešení. GSK umožňuje komerční služby jako mobilní TV s Digital Rights Management ([DRM](/mobilnisite/slovnik/drm/)) a kritické služby jako skupinová komunikace pro veřejnou bezpečnost, kde jsou klíčové jak efektivita, tak důvěrnost.

## Klíčové vlastnosti

- Symetrický klíč sdílený mezi všemi členy definované služební skupiny
- Umožňuje efektivní šifrování vysílacího/multicastového provozu (jedno šifrování pro všechny)
- Integrován do hierarchie klíčů 3GPP (např. odvozen z uživatelského klíče MBMS nebo služebně specifických kořenových klíčů)
- Podporuje periodickou výměnu klíče (rekeying) pro forward secrecy a správu změn členství ve skupině
- Distribuován prostřednictvím zabezpečených unicastových kanálů za použití individuálních bezpečnostních kontextů UE před zahájením skupinové relace
- Používá se k ochraně kritických skupinových služeb, jako jsou MBMS a MCPTT, jak je definováno ve specifikacích 3GPP

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MUK – Multicast User Key](/mobilnisite/slovnik/muk/)
- [MSK – Minimum-shift keying](/mobilnisite/slovnik/msk/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [GSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsk/)
