---
slug: "upa"
url: "/mobilnisite/slovnik/upa/"
type: "slovnik"
title: "UPA – Update Notification Acknowledgment"
date: 2025-01-01
abbr: "UPA"
fullName: "Update Notification Acknowledgment"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upa/"
summary: "Příkaz protokolu Diameter (Update-Notification-Answer) používaný na rozhraní 3GPP S6a/S6d mezi MME/SGSN a HSS. Je to potvrzovací zpráva odeslaná jako odpověď na Update Notification Request (UPR), kter"
---

UPA je potvrzovací zpráva protokolu Diameter odesílaná z HSS na MME/SGSN přes rozhraní S6a/S6d, která potvrzuje úspěšné zpracování notifikace o změně dat účastníka.

## Popis

Update Notification Acknowledgment (UPA) je specifická odpověď (Answer) protokolu Diameter definovaná ve specifikacích rozhraní 3GPP S6a (pro LTE/EPC) a S6d (pro [SGSN](/mobilnisite/slovnik/sgsn/) založené na [GTP](/mobilnisite/slovnik/gtp/) připojené k [HSS](/mobilnisite/slovnik/hss/)). Je to přímá odpověď na příkaz Update Notification Request (UPR). Rozhraní S6a/S6d se používá pro autentizaci, autorizaci a správu mobility mezi Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) a Home Subscriber Server (HSS). Dialog UPR/UPA je klíčový mechanismus, který umožňuje HSS proaktivně informovat MME/SGSN o změnách v profilu nebo stavu účastníka uloženém v HSS.

Technicky je UPA zpráva protokolu Diameter s nastaveným Command-Code na hodnotu 316 (Update-Notification) a s vymazaným bitem 'R' v poli Command Flags, což značí, že se jedná o odpověď (Answer). Je odesílána z MME nebo SGSN zpět na HSS. Primární funkcí UPA je informovat HSS, že MME/SGSN úspěšně přijalo a zpracovalo odpovídající UPR. Zpráva UPA nese [AVP](/mobilnisite/slovnik/avp/) (Attribute-Value Pair) Result-Code, který udává výsledek zpracování. Úspěšné potvrzení by použilo Result-Code jako DIAMETER_SUCCESS (2001).

Zpráva UPA může obsahovat i další relevantní AVP. Například, pokud UPR požadovalo po MME odeslání uživatelských dat, UPA může obsahovat požadovaná data v konkrétních AVP. Tato výměna zajišťuje synchronizaci mezi HSS (hlavní databází) a obslužným uzlem (MME/SGSN) ohledně informací o účastníkovi. To je klíčové pro vynucení změn, jako jsou aktualizované QoS profily, přihlášené Access Point Names ([APN](/mobilnisite/slovnik/apn/)) nebo stav blokování v reálném čase, bez čekání na další periodickou aktualizaci nebo proceduru připojení (attach). Spolehlivé doručení UPA potvrzuje HSS, že obslužný uzel nyní uplatňuje aktualizované parametry účastníka, čímž udržuje konzistentní poskytování služeb v síti.

## K čemu slouží

UPA existuje jako součást spolehlivého notifikačního protokolu pro udržení synchronizace dat účastníka mezi centrálním úložištěm ([HSS](/mobilnisite/slovnik/hss/)) a distribuovanými síťovými uzly (MME/SGSN), které vynucují politiky a spravují relace. Řeší problém zastaralých nebo nekonzistentních dat účastníka v obslužném uzlu, což by mohlo vést k problémům se službou, nesprávným účtováním nebo bezpečnostním rizikům. Před zavedením takových mechanismů často aktualizace profilu účastníka vyžadovala, aby se účastník znovu připojil k síti, nebo spoléhala na nečastou synchronizaci, což bylo neefektivní a pomalé.

Zavedeno v kontextu Evolved Packet Core (EPC) a rozhraní založených na Diameter (Release 11 pro zdokonalení S6a) poskytuje procedura UPR/UPA push model pro aktualizace dat. Motivací bylo podpořit dynamické změny politik a úpravy služeb v reálném čase. Například operátor může okamžitě deaktivovat ztracené zařízení (pomocí IMSI detach) nebo upgradovat služební plán uživatele a HSS může okamžitě informovat obslužné MME, které odpoví pomocí UPA. Tím je zajištěna rychlá reakce sítě a umožněny pokročilé funkce správy účastníků v reálném čase, což zlepšuje jak provozní efektivitu, tak zákaznický zážitek.

## Klíčové vlastnosti

- Odpověď (Answer) protokolu Diameter (Command-Code 316) na rozhraní S6a/S6d.
- Odesílána MME nebo SGSN k potvrzení přijetí a zpracování Update Notification Request (UPR).
- Obsahuje AVP Result-Code udávající úspěch nebo neúspěch aktualizace.
- Umožňuje spolehlivou synchronizaci dat účastníka mezi HSS a obslužným uzlem.
- Podporuje vynucení změn v profilu účastníka v reálném čase (např. QoS, APN, blokování).
- Součást proaktivního notifikačního mechanismu iniciovaného HSS.

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [UPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/upa/)
