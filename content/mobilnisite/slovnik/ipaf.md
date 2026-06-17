---
slug: "ipaf"
url: "/mobilnisite/slovnik/ipaf/"
type: "slovnik"
title: "IPAF – IP Adaptation Function"
date: 2025-01-01
abbr: "IPAF"
fullName: "IP Adaptation Function"
category: "Core Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ipaf/"
summary: "Funkční entita definovaná v raných vydáních 3GPP pro 3GPP IP Multimedia Subsystem (IMS). Funguje jako adaptační vrstva mezi řídicím signálováním s přepojováním okruhů (např. ISUP) a IP protokolem Sess"
---

IPAF je funkční entita v IMS, která poskytuje adaptační vrstvu mezi přepojováním okruhů a SIP, aby umožnila spolupráci s legacy telefonními sítěmi.

## Popis

IP Adaptation Function (IPAF) je element základní sítě specifikovaný v raných fázích architektury IP Multimedia Subsystem (IMS). Jeho hlavní úloha je umožnit bezproblémovou spolupráci mezi paketově přepojovanou, SIP-based doménou IMS a tradičními telefonními sítěmi s přepojováním okruhů, jako je Public Switched Telephone Network (PSTN) nebo legacy Public Land Mobile Network (PLMN). Funkčně funguje jako signalizační brána a překladač protokolů. Nachází se na hranici IMS, často společně nebo jako část Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo specializované Interworking Function ([IWF](/mobilnisite/slovnik/iwf/)).

Architektonicky IPAF komunikuje s [CS](/mobilnisite/slovnik/cs/) sítí pomocí protokolů jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC) přes tradiční SS7 nebo IP-based signalizační transporty. Na straně IMS komunikuje s Call Session Control Functions (CSCFs) pomocí Session Initiation Protocol (SIP). IPAF provádí mapování mezi sémanticky rozdílnými signalizačními zprávami a parametry těchto dvou domén. Například překládá ISUP Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) do SIP INVITE requestu, zajišťující přesné přenesení čísel volaného/volajícího, možností nosiče a indikátorů průběhu hovoru. Také zajišťuje překlad v opačném směru pro odpovědi a signalizaci během hovoru.

Jak funguje zahrnuje stavové řízení session. IPAF udržuje stav každého hovoru mezi doménami, koreluje CS část a IMS část. Modifikuje SIP hlavičky a SDP těla aby odpovídaly charakteristikám CS nosiče a naopak. Dále může komunikovat s dalšími IMS funkcemi jako Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) pro rozhodování o směrování, když hovor vzniká v IMS a přechází do CS sítě. I když se následné IMS architektury vyvíjely a upřesňovaly tyto funkce spolupráce (s MGCF přebírající více prominentní, integrovanou roli), IPAF reprezentoval počáteční konceptuální rozklad adaptační vrstvy, objasňující oddělení adaptace signalizace od konverze médií (zajišťované Media Gateway) a logiky řízení hovoru.

## K čemu slouží

IPAF byl vytvořen aby řešil kritický raný problém při nasazení IMS: zpětnou kompatibilitu. Když 3GPP definoval IMS ve vydání 5 jako budoucí all-IP platformu pro poskytování služeb, existovala rozsáhlá instalovaná základna sítí a účastníků s přepojováním okruhů. Aby IMS bylo životaschopné, muselo být možné spojení s tímto legacy světem, aby umožnilo tok hlasových a dalších služeb mezi IP a [CS](/mobilnisite/slovnik/cs/) účastníky. IPAF poskytoval specializovanou funkční entitu pro řízení této komplexní signalizační spolupráce.

Problém který řešil byl základní nekompatibilita protokolů. CS sítě používaly stavové, spojením orientované signalizaci jako ISUP, navržené pro dedikované časové sloty. IMS používalo bezstavové, textové SIP, navržené pro IP session. Bez adaptační funkce by hovory mezi doménami byly nemožné. IPAF abstrahoval tuto komplexnost, umožňující IMS core elementům (CSCFs) komunikovat pomocí SIP, zatímco IPAF zajišťoval překlad do/ze CS světa. Toto umožnilo postupnou migraci sítě, umožňující operatorům zavést IMS ostrovy, které mohly stále obsluhovat a spojovat se s celou základnou účastníků. Jeho specifikace pomohla formalizovat mapující pravidla a chování potřebné pro spolehlivou spolupráci, které byly následně absorbovány a rozšířeny v širší specifikaci MGCF.

## Klíčové vlastnosti

- Překlad protokolů mezi SIP a ISUP/BICC
- Signalizační spolupráce pro řízení hovoru
- Mapování adresování a číselných informací
- Adaptace charakteristik nosiče a služby
- Stavové řízení pro části hovoru mezi doménami
- Interface směrem k CS síti i IMS core

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [BGCF – Breakout Gateway Control Function](/mobilnisite/slovnik/bgcf/)

## Definující specifikace

- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements

---

📖 **Anglický originál a plná specifikace:** [IPAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipaf/)
