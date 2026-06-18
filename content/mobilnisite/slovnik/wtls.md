---
slug: "wtls"
url: "/mobilnisite/slovnik/wtls/"
type: "slovnik"
title: "WTLS – Wireless Transport Layer Security"
date: 2025-01-01
abbr: "WTLS"
fullName: "Wireless Transport Layer Security"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wtls/"
summary: "Bezpečnostní protokol pro bezdrátové aplikace, založený na TLS, poskytující integritu dat, soukromí a autentizaci. Byl klíčový pro zabezpečení časných mobilních datových služeb, jako je WAP, a byl při"
---

WTLS je bezpečnostní protokol Wireless Transport Layer Security, založený na TLS, který zajišťuje integritu dat, soukromí a autentizaci pro zabezpečení časných mobilních datových služeb, jako je WAP.

## Popis

Wireless Transport Layer Security (WTLS) je bezpečnostní protokol definovaný v architektuře Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)), speciálně navržený pro provoz přes přenosové služby s potenciálně vysokou latencí a nízkou šířkou pásma. Funkčně je analogický protokolu Transport Layer Security ([TLS](/mobilnisite/slovnik/tls/)) používanému na drátovém internetu, ale je optimalizován pro omezení mobilních sítí a zařízení. WTLS pracuje na transportní vrstvě zásobníku protokolů WAP, nachází se nad Wireless Datagram Protocol ([WDP](/mobilnisite/slovnik/wdp/)) a pod Wireless Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)). Jeho hlavní úlohou je vytvoření zabezpečeného komunikačního kanálu mezi klientem WAP (např. prohlížečem v mobilním telefonu) a bránou nebo serverem WAP, který zajišťuje důvěrnost, integritu a autenticitu vyměňovaných dat.

Protokol pracuje v několika odlišných fázích: fázi handshake, fázi změny šifrovací specifikace a fázi záznamového protokolu. Během handshake klient a server vyjednávají kryptografické algoritmy, vzájemně se autentizují (pomocí certifikátů nebo předem sdílených klíčů) a stanoví sdílené tajné klíče. WTLS podporuje různé kryptografické sady, včetně těch založených na [RSA](/mobilnisite/slovnik/rsa/) a Elliptic Curve Cryptography ([ECC](/mobilnisite/slovnik/ecc/)), přičemž ECC je zvláště preferována pro svou efektivitu na zařízeních s omezenými zdroji. Po úspěšném handshake signalizuje zpráva změny šifrovací specifikace přechod na nově vyjednanou šifrovací sadu. Následně přebírá kontrolu záznamový protokol, který je zodpovědný za fragmentaci, kompresi (volitelně), aplikaci Message Authentication Code ([MAC](/mobilnisite/slovnik/mac/)), šifrování dat a jejich přenos přes podkladový transport WDP.

Klíčové architektonické komponenty WTLS zahrnují správu stavového spojení, podporu pro datagramové a spojením orientované transporty a mechanismy pro zvládání ztráty a přeuspořádání paketů, běžných v bezdrátových spojích. Poskytuje několik tříd služeb (WTLS třída 1, 2 a 3) nabízejících různé úrovně zabezpečení, od jednoduchého šifrování až po vzájemnou autentizaci s neodmítnutelností. Protokol také zahrnuje funkce jako optimalizované handshake (zkrácené handshake pro obnovení relace) a explicitní pořadová čísla pro potírání replay útoků. Jeho integrace do zásobníku WAP znamenala, že musel interoperovat s bránou WAP, která typicky prováděla překlad protokolů mezi doménou zabezpečenou WTLS a internetovou doménou zabezpečenou TLS, což byl bod zavádějící specifická bezpečnostní hlediska týkající se ukončení šifrování na bráně.

## K čemu slouží

WTLS byl vytvořen, aby řešil kritickou potřebu zabezpečení na rostoucím trhu mobilních datových služeb umožněných Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)) na konci 90. let a začátku 21. století. Standardní internetový bezpečnostní protokol TLS (a jeho předchůdce SSL) byl navržen pro relativně stabilní, vysokorychlostní drátová připojení a byl výpočetně náročný, což jej činilo nevhodným pro omezené prostředí časných mobilních telefonů s omezeným výpočetním výkonem, pamětí a životností baterie, pracujících přes úzkopásmové, vysoce latentní bezdrátové kanály jako GSM Circuit Switched Data nebo SMS.

Protokol řešil problém poskytování end-to-end bezpečnostních záruk – důvěrnosti, integrity dat a autentizace – pro aplikace jako mobilní bankovnictví, elektronický obchod a korporátní přístup, kde se přenášela citlivá data. Umožnil poskytovatelům služeb nabízet důvěryhodné služby přes veřejné bezdrátové sítě. Klíčovou motivací bylo vytvořit bezpečnostní vrstvu, která by odolala specifickým hrozbám bezdrátového prostředí, jako je odposlech rádiového spoje a vyšší potenciál pro ztrátu paketů, aniž by ukládala nepřiměřenou režii. Definováním přizpůsobeného protokolu umožnily 3GPP a WAP Forum mobilnímu ekosystému nasazovat zabezpečené služby roky předtím, než byly přístroje a sítě dostatečně výkonné, aby efektivně provozovaly plné zásobníky internetového TLS.

## Klíčové vlastnosti

- Optimalizovaný handshake protokol s podporou zkrácených handshake pro snížení latence a režie
- Podpora více kryptografických sad včetně efektivní Elliptic Curve Cryptography (ECC)
- Poskytování různých tříd bezpečnostních služeb (třída 1, 2 a 3) pro flexibilní implementaci
- Podpora datagramového transportu s explicitními pořadovými čísly pro prevenci replay útoků přes nespolehlivé spoje
- Volitelná komprese dat na vrstvě záznamového protokolu pro úsporu šířky pásma
- Správa stavového spojení umožňující bezpečné pozastavení a obnovení relace

## Související pojmy

- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [WDP – Wireless Datagram Protocol](/mobilnisite/slovnik/wdp/)
- [WSP – Web Service Provider](/mobilnisite/slovnik/wsp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [WTLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wtls/)
