---
slug: "wtp"
url: "/mobilnisite/slovnik/wtp/"
type: "slovnik"
title: "WTP – Wireless Transaction Protocol"
date: 2025-01-01
abbr: "WTP"
fullName: "Wireless Transaction Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wtp/"
summary: "Odlehčený transakčně orientovaný protokol ve WAP zásobníku poskytující spolehlivé služby typu požadavek/odpěď. Spravuje efektivní výměnu datových jednotek mezi WAP klientem a serverem, optimalizuje vý"
---

WTP je odlehčený transakčně orientovaný protokol ve WAP zásobníku, který poskytuje spolehlivé služby typu požadavek/odpověď a spravuje efektivní výměnu dat mezi klientem a serverem s segmentací a opětovným sestavením pro bezdrátové spoje.

## Popis

Wireless Transaction Protocol (WTP) je protokol vrstvy 4 (transportní vrstva) v architektuře Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)), navržený k poskytování efektivních transakčních služeb nad potenciálně nespolehlivými bezdrátovými datagramovými přenosy. Nachází se nad Wireless Datagram Protocol ([WDP](/mobilnisite/slovnik/wdp/)) a pod Wireless Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)) nebo přímo pod aplikacemi. Na rozdíl od spojově orientovaných protokolů jako TCP je WTP transakčně orientovaný, což znamená, že je navržen pro krátkodobé interakce typu požadavek/odpověď typické pro webové prohlížení a telemetrii, čímž se vyhýbá režii spojení pro každou výměnu dat. Jeho hlavní funkcí je zajistit spolehlivé, nezdvojené doručování zpráv mezi WAP klientem (iniciátorem) a WAP serverem (responderem).

WTP funguje pomocí tří tříd transakčních služeb, z nichž každá nabízí jinou úroveň spolehlivosti a funkcionality pro různé potřeby aplikací. Třída 0 poskytuje nespolehlivou vyvolávací zprávu bez výsledné zprávy, vhodnou pro jednosměrná oznámení. Třída 1 poskytuje spolehlivou vyvolávací zprávu bez výsledné zprávy, zajišťující doručení požadavku, ale neočekávající odpověď (např. spolehlivý push). Třída 2, nejběžnější, poskytuje spolehlivou vyvolávací zprávu následovanou spolehlivou výslednou zprávou, implementující klasickou spolehlivou transakci požadavek/odpověď. Protokol používá jedinečný transakční identifikátor ([TID](/mobilnisite/slovnik/tid/)) ke spárování požadavků s odpověďmi. Zahrnuje mechanismy segmentace a opětovného sestavení ([SAR](/mobilnisite/slovnik/sar/)) pro zpracování velkých zpráv překračujících maximální přenosovou jednotku ([MTU](/mobilnisite/slovnik/mtu/)) podkladového přenosu, rozděluje je na menší WTP protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) pro přenos.

Vnitřní fungování WTP zahrnuje stavové automaty pro iniciátora i respondera. Klíčové procedury zahrnují zahájení transakce, kdy iniciátor odešle Invoke PDU; potvrzení, používající Ack PDU pro spolehlivost; a dokončení transakce s Result PDU (pro třídu 2). WTP používá selektivní opakování založené na negativních potvrzeních ([NACK](/mobilnisite/slovnik/nack/)) nebo časovačích pro obnovu ze ztracených paketů, což je efektivnější než jednoduchý go-back-N v prostředí se ztrátami. Zahrnuje také funkci konkatenace/dekonkatenace pro zabalení více PDU do jedné jednotky dat služby (SDU) nižší vrstvy, čímž snižuje režii hlaviček. Poskytnutím těchto služeb WTP abstrahuje nespolehlivost a charakteristiky podkladové sítě a nabízí konzistentní rozhraní pro vyšší vrstvu WSP pro správu relací a výměnu aplikačních dat.

## K čemu slouží

WTP byl vyvinut k řešení neefektivity používání tradičních internetových protokolů jako TCP na vysoce latencních, nízkopásmových a na ztráty náchylných bezdrátových spojích sítí 2G a raných 2.5G (např. GSM CSD, GPRS). TCP třícestný handshake, mechanismy řízení zahlcení a orientace na proud bajtů zaváděly významnou latenci a režii pro krátké transakční výměny charakteristické pro rané mobilní webové prohlížení (WAP browsing) a telemetrické služby. Tento nesoulad vedl ke špatné uživatelské zkušenosti a plýtvání vzácnými rádiovými zdroji.

Transakčně orientovaný design protokolu byl motivován potřebou odlehčeného, na zprávy založeného transportu, který by mohl poskytnout spolehlivost tam, kde je potřeba, bez plné režie trvalého spojení. Řešil problém efektivní a spolehlivé komunikace typu požadavek/odpověď pro omezená zařízení a sítě. Nabídkou různých tříd služeb umožnil vývojářům aplikací zvolit vhodnou úroveň spolehlivosti a vyhnout se zbytečným potvrzením pro jednosměrný provoz. Integrovaná segmentace a opětovné sestavení spolu s konkatenací byly klíčové pro optimalizaci využití malých paketů pevné velikosti běžných u některých bezdrátových přenosů a pro zpracování webových objektů větších než jeden síťový paket. WTP byl klíčovým prvkem pro ekosystém WAP 1.x, umožňující interaktivním službám fungovat s přiměřeným výkonem v technologických limitech své doby.

## Klíčové vlastnosti

- Tři transakční třídy (0, 1 a 2) nabízející volitelné úrovně spolehlivosti pro vyvolávací a výsledné zprávy
- Integrovaná segmentace a opětovné sestavení (SAR) pro zpracování zpráv větších než MTU podkladového přenosu
- Konkatenace a dekonkatenace více PDU ke snížení přenosové režie
- Efektivní mechanismus opakování využívající transakční identifikátory a negativní potvrzení (NACK)
- Odlehčený, transakčně orientovaný design vyhýbající se udržování stavu trvalého spojení
- Explicitní nespojová operace nad datagramovými transporty poskytovanými WDP

## Související pojmy

- [WDP – Wireless Datagram Protocol](/mobilnisite/slovnik/wdp/)
- [WSP – Web Service Provider](/mobilnisite/slovnik/wsp/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wtp/)
