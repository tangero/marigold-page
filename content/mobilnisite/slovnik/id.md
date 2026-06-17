---
slug: "id"
url: "/mobilnisite/slovnik/id/"
type: "slovnik"
title: "ID – Identity / Identifier"
date: 2025-01-01
abbr: "ID"
fullName: "Identity / Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/id/"
summary: "Základní koncept v sítích 3GPP představující jedinečný název nebo označení pro síťovou entitu, uživatele nebo prostředek. Je klíčový pro adresování, směrování, autentizaci a správu dat účastníků v cel"
---

ID je jedinečný název nebo označení pro síťovou entitu, uživatele nebo prostředek, který je zásadní pro adresování, směrování, autentizaci a správu dat účastníků v sítích 3GPP.

## Popis

Ve specifikacích 3GPP je ID (identita nebo identifikátor) základním datovým prvkem používaným k jedinečnému pojmenování, označení nebo adresování konkrétní entity v telekomunikační síti. Tato entita může být uživatel (účastník), zařízení (User Equipment – UE), síťový uzel, služba nebo konkrétní relace. Tento koncept je všudypřítomný a slouží jako základní kámen síťových operací, umožňuje funkce jako směrování, správu mobility, bezpečnostní procedury a poskytování služeb. Identifikátory jsou definovány s konkrétními formáty, rozsahy platnosti a životností a jejich správa je kritická pro integritu a funkčnost sítě.

Z architektonického hlediska jsou ID zabudována do různých protokolů a rozhraní. Například v jádru sítě se pro primární identifikaci účastníka používají identifikátory jako International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) nebo Subscription Permanent Identifier (SUPI). V rádiové přístupové síti (RAN) jsou identifikátory jako Radio Network Temporary Identifier (RNTI) dynamicky přidělovány zařízením UE pro efektivní řízení rádiových prostředků. Specifikace, například 3GPP TS 25.423 pro uživatelské rovinné protokoly rozhraní IUTRAN, definují, jak jsou tyto identifikátory přenášeny a interpretovány v konkrétních protokolových datových jednotkách (PDU), aby bylo zajištěno správné dorozumívání mezi uzly a správa kontextu.

Způsob fungování ID závisí na jeho typu. Trvalé identifikátory, jako je IMSI, jsou uloženy v SIM kartě účastníka a v síťovém serveru Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a používají se pro základní procedury, jako je počáteční připojení a autentizace. Dočasné identifikátory, jako je Globally Unique Temporary Identity ([GUTI](/mobilnisite/slovnik/guti/)) v 5G, přiděluje síť za účelem ochrany trvalé identity uživatele na rádiovém rozhraní a pro usnadnění efektivního pagingu a servisních požadavků. Síť neustále mapuje mezi různými identifikátory (např. ze SUPI na [5G-GUTI](/mobilnisite/slovnik/5g-guti/)), jak se uživatel pohybuje nebo zahajuje relace, a udržuje stav v různých síťových funkcích, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G.

Jeho role je mnohostranná. Především umožňuje jednoznačnou identifikaci, což je předpoklad každého komunikačního systému. Pro mobilitu umožňují ID síti sledovat oblast polohy uživatele. Pro zabezpečení jsou vázány na autentizační klíče a certifikáty. Pro kvalitu služeb (QoS) jsou propojeny s konkrétními profilů politiky. Pro účtování se používají ke korelaci záznamů o použití s konkrétním předplatným. Správné zacházení s identifikátory a jejich ochrana, zejména těch trvalých, je proto kritickým aspektem síťové bezpečnosti a soukromí účastníků.

## K čemu slouží

Účelem konceptu ID v 3GPP je poskytnout standardizovanou, jednoznačnou metodu pro pojmenování a adresování všech entit zapojených do mobilní komunikace. Bez takového základního systému by nebylo možné směrovat hovory a data, autentizovat uživatele, spravovat mobilitu nebo účtovat služby. Řeší základní problém „kdo je kdo“ a „co je co“ v rozsáhlé, distribuované a interoperabilní globální síti.

Historicky, jak se mobilní sítě vyvíjely z jednoduchých okruhově přepínaných systémů na složité architektury založené na paketovém přepínání IP, rostla potřeba bohaté a hierarchické sady identifikátorů. Rané systémy jako GSM zavedly [IMSI](/mobilnisite/slovnik/imsi/), což byl průlom pro globální roaming. Každá následující generace (3G/UMTS, 4G/LTE, 5G) zaváděla nové identifikátory a vylepšovala stávající, aby řešila nové požadavky, jako je lepší ochrana soukromí (např. použití dočasných identifikátorů pro maskování trvalých na rádiovém spoji), podpora heterogenního síťového přístupu a oddělení identity uživatele od identity zařízení.

Vytváření a vývoj identifikátorů je motivován klíčovými výzvami: zajištění globální jedinečnosti pro podporu roamingu, zvýšení bezpečnosti minimalizací vystavení trvalých identit, zlepšení efektivity sítě umožněním používání lokálních, krátkých identifikátorů pro častou signalizaci a umožnění nových servisních paradigmat, jako je síťové krájení (network slicing) a masivní IoT, kde může mít jediný uživatel nebo zařízení více souběžných identit pro různé logické sítě nebo služby. Rámec ID definovaný ve specifikacích 3GPP poskytuje potřebný nástrojový soubor pro tyto funkce.

## Klíčové vlastnosti

- Jedinečnost v rámci definovaného rozsahu (globální, síťová, lokální)
- Strukturovaný formát často definovaný standardy (např. MCC, MNC, MSIN pro IMSI)
- Podpora jak trvalých (předplatné), tak dočasných (relačních) identit
- Mapování a korelace mezi různými typy identifikátorů síťovými funkcemi
- Ochranné mechanismy (např. šifrování, skrytí) pro soukromí
- Použití ve všech síťových doménách: UE, RAN, jádro sítě a externí sítě

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/id/)
