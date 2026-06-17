---
slug: "csgid"
url: "/mobilnisite/slovnik/csgid/"
type: "slovnik"
title: "CSGID – Closed Subscriber Group Identity"
date: 2025-01-01
abbr: "CSGID"
fullName: "Closed Subscriber Group Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csgid/"
summary: "Jedinečný identifikátor pro uzavřenou skupinu účastníků (CSG), který definuje množinu účastníků s oprávněním přístupu ke konkrétní buňce, typicky k Home NodeB (HNB) nebo Home eNodeB (HeNB). Umožňuje o"
---

CSGID je jedinečný identifikátor pro uzavřenou skupinu účastníků (Closed Subscriber Group), který definuje, kteří účastníci mají oprávnění přistupovat ke konkrétní restriktivní buňce, jako je např. femtobuňka.

## Popis

Identita uzavřené skupiny účastníků (CSGID) je základní identifikátor v sítích 3GPP, speciálně navržený pro správu přístupu k buňkám fungujícím s omezeným členstvím. Jedná se o 27bitovou hodnotu, která jednoznačně identifikuje jednu uzavřenou skupinu účastníků ([CSG](/mobilnisite/slovnik/csg/)). CSG je logická skupina účastníků (User Equipment - UE), kteří mají oprávnění přistupovat k jedné nebo více buňkám určitého typu, především k Home NodeBs ([HNB](/mobilnisite/slovnik/hnb/)) v 3G UMTS nebo k Home eNodeBs (HeNB) v 4G LTE, které jsou souhrnně označovány jako femtobuňky nebo obecněji jako buňky uzavřené skupiny účastníků. CSGID je vysílán buňkou v jejích systémových informacích, což umožňuje UE buňku identifikovat a určit, zda jsou autorizovanými členy přidružené CSG.

Z architektonického hlediska je CSGID klíčovou součástí konceptu CSG, který byl zaveden pro podporu rezidenčních, podnikových nebo hotspotových nasazení, kde jsou rádiové zdroje určeny pro omezenou skupinu uživatelů. Tento identifikátor je uložen ve dvou kritických síťových prvcích: v UE a v jádru sítě. Každé UE si udržuje tzv. CSG Whitelist, což je seznam CSGID (a volitelně jejich přidružených kódů lokalizační oblasti nebo PLMN ID), ke kterým účastník patří. Tento whitelist může být provozovatelem zřízen prostřednictvím [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) mechanismů nebo ručně nakonfigurován. V jádru sítě, konkrétně v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro LTE/EPC nebo v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro UMTS, profily účastníků obsahují jejich autorizované CSGID. Běhy mobilních procedur, jako je předávání spojení nebo počáteční připojení, síť ověřuje členství UE v CSG proti tomuto profilu.

Operační postup zahrnuje několik kroků. Když UE detekuje CSG buňku, přečte vysílaný CSGID. UE poté zkontroluje svůj interní CSG Whitelist. Pokud je CSGID přítomen, UE se považuje za člena a může se pokusit o přístup k buňce, obvykle s vyšší prioritou (pomocí parametrů pro výběr/převýběr buňky specifických pro CSG). Během přístupové procedury UE zahrne CSGID do svých signalizačních zpráv do sítě, například v [RRC](/mobilnisite/slovnik/rrc/) Connection Setup nebo Attach Request. Síť, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) v UMTS, ověří tento CSGID proti profilu účastníka získanému z HSS/HLR. Pokud je ověření úspěšné, je přístup povolen; pokud ne, je UE odmítnuto nebo přesměrováno na vhodnou makrobuňku. Tento mechanismus zajišťuje, že pouze autorizovaní účastníci mohou využívat zdroje CSG buňky, čímž se zabraňuje neoprávněnému přístupu a potenciálním interferencím nebo přetížení.

CSGID hraje klíčovou roli také v hybridních režimech přístupu, kde může buňka fungovat v 'hybridním' režimu, což umožňuje připojení jak členům CSG (s prioritním přístupem), tak i nečlenům (s možným omezením zdrojů). V takových případech je CSGID stále vysílán a síť jej používá k rozlišení mezi UE členy a nečleny pro účely řízení přístupu a účtování. CSGID je navíc nedílnou součástí správy a optimalizace sítě, což operátorům umožňuje sledovat vzorce využití, provádět cílené účtování a řídit interference v hustých nasazeních femtobuněk. Jeho standardizovaný formát zajišťuje interoperabilitu mezi zařízeními různých výrobců a konzistentní chování v prostředích s více dodavateli.

## K čemu slouží

CSGID byl vytvořen, aby řešil rostoucí potřebu řízeného, restriktivního přístupu v nasazeních small cell, zejména femtobuněk (Home NodeBs a Home eNodeBs), které se objevily koncem první dekády 21. století. Před jeho zavedením nabízely mobilní sítě primárně otevřený přístup (jakýkoli účastník se mohl připojit k jakékoli buňce) nebo v omezené míře používaly proprietární metody pro omezení přístupu, které nebyly standardizované a vedly k problémům s interoperabilitou. Když operátoři začali nasazovat femtobuňky v domácnostech a firmách za účelem zlepšení vnitřního pokrytí a odlehčení provozu v makrosíti, vznikla jasná potřeba omezit přístup k těmto buňkám pouze na konkrétní účastníky – například pouze na členy domácnosti nebo zaměstnance společnosti. Bez standardizovaného mechanismu by se potenciálně mohli připojit neoprávnění uživatelé, čímž by spotřebovávali šířku pásma určenou vlastníkovi a vyvolávali obavy ohledně bezpečnosti a účtování.

CSGID tyto problémy řeší tím, že poskytuje standardizovaný, operátorem řízený identifikátor, který definuje uzavřenou skupinu účastníků. Umožňuje jádru sítě vynucovat přístupové politiky na základě profilů účastníků, což zajišťuje, že pouze autorizovaná UE se mohou připojit k CSG buňce nebo na ní pobývat. To je klíčové z několika důvodů: chrání investici vlastníka femtobuňky tím, že mu garantuje vyhrazenou kapacitu, zvyšuje bezpečnost tím, že brání neoprávněnému přístupu k tomu, co je v podstatě privátním rozšířením sítě, a umožňuje operátorům nabízet diferencované služby a tarify (např. speciální sazby pro využití v domácí zóně). Historicky se tento koncept vyvinul z dřívějších funkcí mobilních sítí, jako je lokalizační oblast (LA) nebo směrovací oblast (RA), ale ty byly pro omezení na úrovni buňky příliš hrubozrnné. CSGID, zavedený v 3GPP Release 8 spolu s LTE a vylepšeným UMTS, poskytl jemnozrnná, škálovatelná řešení potřebná pro masové nasazení femtobuněk.

CSGID navíc usnadňuje správu a optimalizaci sítě. Díky jasné identifikaci CSG buněk mohou operátoři implementovat specifické mobilní politiky – například UE lze nakonfigurovat tak, aby upřednostňovala svou domovskou CSG buňku pro lepší kvalitu služby. Také napomáhá řízení interference v hustých nasazeních, protože síť dokáže rozlišit mezi buňkami obsluhujícími uzavřené skupiny a těmi, které nabízejí otevřený přístup. Vytvoření CSGID bylo motivováno posunem průmyslu k heterogenním sítím (HetNets), kde small cell doplňují makrovrstvu, a jeho standardizace zajistila konzistentní přístup napříč globálními operátory, zabránila fragmentaci a umožnila úspory z rozsahu pro výrobce zařízení.

## Klíčové vlastnosti

- 27bitový jedinečný identifikátor pro uzavřenou skupinu účastníků (CSG)
- Vysílán v systémových informacích buňky pro detekci UE
- Uložen v CSG Whitelistu UE pro ověření členství
- Ověřován jádrem sítě (HSS/HLR, MME/SGSN) během přístupových procedur
- Podporuje hybridní režim přístupu pro diferencované zacházení s členy/nečleny
- Umožňuje operátorem řízené zřizování prostřednictvím OTA nebo ruční konfigurace

## Související pojmy

- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)
- [HNB – Home Node B](/mobilnisite/slovnik/hnb/)
- [HENB – Home Enhanced Node B](/mobilnisite/slovnik/henb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CSGID na 3GPP Explorer](https://3gpp-explorer.com/glossary/csgid/)
