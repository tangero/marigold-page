---
slug: "gra"
url: "/mobilnisite/slovnik/gra/"
type: "slovnik"
title: "GRA – GERAN Registration Area"
date: 2025-01-01
abbr: "GRA"
fullName: "GERAN Registration Area"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gra/"
summary: "GERAN Registration Area (GRA) je logické seskupení buněk v 2G GSM/EDGE Radio Access Network (GERAN). Definuje oblast, pro kterou mobilní zařízení provádí registraci polohy a vysílání (paging), což umo"
---

GRA je logické seskupení buněk v 2G GERAN, které definuje oblast pro registraci polohy mobilního zařízení a vysílání (paging) za účelem efektivního řízení mobility.

## Popis

[GERAN](/mobilnisite/slovnik/geran/) Registration Area (GRA) je klíčový koncept v řízení mobility 2G GSM a [EDGE](/mobilnisite/slovnik/edge/) sítí. Je to logická oblast, definovaná v konfiguraci sítě, která se skládá z jedné nebo více Location Areas ([LA](/mobilnisite/slovnik/la/)) nebo Routing Areas ([RA](/mobilnisite/slovnik/ra/)). Location Area je skupina buněk, kde mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) v nečinném stavu (idle mode) může pohybovat bez provedení aktualizace polohy, zatímco Routing Area je podoblast Location Area používaná pro [GPRS](/mobilnisite/slovnik/gprs/)/EDGE služby s přepojováním paketů. GRA agreguje tyto oblasti, aby vytvořila větší zónu pro účely registrace.

Fungování je založeno na stavech mobilního zařízení. Když je mobilní zařízení zapnuto nebo přejde do nové GRA, musí provést proceduru aktualizace GRA s síťou. Tato procedura informuje Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) a/nebo Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v jádru sítě o aktuální GRA zařízení. Následně, když zařízení pohybuje mezi buněk, které všechny patří do stejné GRA, nejsou vyvolány další aktualizace polohy. To významně snižuje signalizační provoz na rádiovém rozhraní a uvnitř jádra sítě. Když pro zařízení přijde příchozí hovor nebo paketová session, síť vysílá (paging) přes všechny buněk v celé GRA, kde je zařízení registrované, aby bylo zařízení lokalizované.

Architektura zahrnuje koordinaci mezi Radio Access Network (GERAN BSS - Base Station System) a Core Network (CN). Identita GRA je vysílána na BCCH (Broadcast Control Channel) každé bunky. Mobilní zařízení čte tuto identitu a porovná ji s uloženou GRA. Nesoulad vyvolá proceduru aktualizace. Síťový operátor definuje hranice GRA při plánování sítě, vyvažuje kompromis mezi zatížením vysílání (paging) (větší GRA znamená vysílání přes více buněk) a signalizací aktualizace polohy (menší GRA znamená častější aktualizace). Koncept GRA je klíčový pro škálovatelné řízení mobility, umožňuje síťám efektivně obsluhovat velké množství zařízení v nečinném stavu minimalizací nepotřebné signalizace pro lokální pohyby, zatímco jsou stále schopné doručovat služby, když je to potřebné.

## K čemu slouží

GRA byla zaváděna pro optimalizaci signalizace řízení mobility v GSM/GPRS/EDGE sítích. Základní problém, který řeší, je kompromis mezi signalizací aktualizace polohy a signalizací vysílání (paging). Bez hierarchické struktury oblastí jako GRA by mobilní zařízení muselo provést aktualizaci polohy pokaždé, když překročí hranici Location Area (LA). V hustých urbanních prostředích s malými bunkami by to mohlo vést k nadměrnému a neudržitelnému zatížení signalizace na síť a baterii zařízení.

Před koncepty jako GRA (a její protějšek v UMTS, URA) bylo řízení mobility primárně založeno na Location Areas a Routing Areas. Vytvoření GRA poskytlo další, větší registrační oblast. To bylo motivované potřebou efektivněji podporovat zařízení s vysokou mobilitou nebo zařízení, které jsou převážně v nečinném stavu (idle mode) (například IoT senzory). Díky tomu, že zařízení může pohybovat přes více LA/RA bez aktualizace jádra sítě, GRA snižuje signalizační kongesci, šetří životnost baterie zařízení a zlepšuje celkovou škálovatelnost sítě. Je to základní technika pro řízení milionů zařízení v mobilní síti, což je výzva, která se stala více výrazná s příchodem neustále připojených služeb s přepojováním paketů přes GPRS a EDGE.

## Klíčové vlastnosti

- Logické seskupení jedné nebo více Location Areas (LA) a/nebo Routing Areas (RA)
- Snižuje frekvenci signalizace aktualizace polohy pro mobilní zařízení v nečinném stavu (idle)
- Vysílání (paging) je prováděno přes celou GRA pro lokalizaci zařízení
- Identita GRA vysílána na BCCH každé bunky
- Konfigurovatelné síťovými operátory pro vyvážení zatížení vysílání (paging) a aktualizací
- Základní pro efektivní řízení mobility v nečinném stavu (idle mode) v GERAN

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.130** (Rel-19) — Iur-g Interface Overview
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gra/)
