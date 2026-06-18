---
slug: "bt"
url: "/mobilnisite/slovnik/bt/"
type: "slovnik"
title: "BT – Business Trunking"
date: 2025-01-01
abbr: "BT"
fullName: "Business Trunking"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bt/"
summary: "Business Trunking (BT) je standardizovaná služba podle 3GPP, která podnikům umožňuje nahradit tradiční PBX systémy cloudovou telefonii přes mobilní sítě. Poskytuje podnikové hlasové, video a messaging"
---

BT je standardizovaná služba podle 3GPP, která podnikům umožňuje nahradit tradiční PBX systémy cloudovou telefonii přes mobilní sítě.

## Popis

Business Trunking je komplexní servisní architektura definovaná ve specifikacích 3GPP, především v TS 22.519, která poskytuje podnikové komunikační služby přes mobilní sítě. Služba umožňuje mobilním operátorům ([MNO](/mobilnisite/slovnik/mno/)) a poskytovatelům služeb nabízet PBX-podobnou funkcionalitu podnikovým účastníkům, kteří používají svá mobilní zařízení jako primární podnikové koncové body. V jádru BT nahrazuje potřebu fyzických stolních telefonů a lokálních ústředen (Private Branch Exchange, [PBX](/mobilnisite/slovnik/pbx/)) využitím IP Multimedia Subsystem (IMS) mobilní sítě pro poskytování služeb.

Architektura Business Trunkingu integruje několik síťových komponent pro poskytování podnikových komunikačních služeb. Mezi klíčové prvky patří IMS core pro řízení relací a zpracování médií, Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro správu dat účastníků a specializované Application Servers ([AS](/mobilnisite/slovnik/as/)), které hostí logiku business trunkingu. Tyto Application Servers implementují funkce jako směrování hovorů na základě podnikových číslovacích plánů, integraci s firemním adresářem, pravidla přesměrování hovorů a konferenční spojování. Služba komunikuje s podnikovými [IT](/mobilnisite/slovnik/it/) systémy prostřednictvím standardizovaných rozhraní, což umožňuje synchronizaci s firemními adresáři jako [LDAP](/mobilnisite/slovnik/ldap/) nebo Active Directory.

Z provozního pohledu Business Trunking funguje tak, že asociuje mobilní účastníky s konkrétními podnikovými profily uloženými v síti. Když účastník BT zahájí nebo přijme hovor, IMS core směruje relaci přes Business Trunking Application Server, který aplikuje podnikově specifické politiky a funkce. To zahrnuje překlad mezi veřejnými telefonními čísly a interními příponami, aplikaci omezení hovorů na základě času nebo cíle a poskytování pokročilých funkcí jako parkování hovoru, jeho převzetí nebo přepojení. Služba podporuje jak hlasovou, tak video komunikaci, přičemž mechanismy kvality služeb (QoS) zajišťují odpovídající prioritu pro podnikový provoz.

Business Trunking hraje klíčovou roli v moderní podnikové komunikaci tím, že překlenuje propast mezi mobilními sítěmi a požadavky podnikové telefonie. Umožňuje poskytovat funkcionalitu tradičně spojovanou s pevnými PBX systémy i na mobilní zařízení, včetně přímého volání (DID), automatického operátora, vyhledávacích skupin a nahrávání hovorů. Služba se integruje s existujícími podnikovými číslovacími plány a může podporovat hybridní nasazení, kde někteří uživatelé zůstávají na tradičních PBX systémech, zatímco jiní migrují na mobilní služby BT. Tato flexibilita umožňuje podnikům postupně přecházet na mobilně orientovanou komunikaci při zachování stávajících telefonních funkcí a uživatelského zážitku.

Bezpečnostní a správní aspekty jsou nedílnou součástí implementací Business Trunkingu. Služba zahrnuje autentizační mechanismy, které ověřují jak identitu mobilního účastníka, tak jeho autorizaci k použití konkrétních podnikových funkcí. Administrativní rozhraní umožňují podnikovým IT pracovníkům spravovat uživatelské profily, konfigurovat pravidla směrování hovorů a generovat podrobné záznamy o hovorech ([CDR](/mobilnisite/slovnik/cdr/)) pro fakturaci a analýzu. Business Trunking také podporuje zpracování tísňových hovorů s odpovídajícími informacemi o poloze a zvýhodněným zacházením, čímž zajišťuje soulad s regulačními požadavky na podnikové telefonní služby.

## K čemu slouží

Business Trunking byl vytvořen, aby řešil rostoucí potřebu podniků modernizovat svou komunikační infrastrukturu a zároveň využít všudypřítomnost a flexibilitu mobilních sítí. Před standardizací BT podniky značně spoléhaly na pevné [PBX](/mobilnisite/slovnik/pbx/) systémy, které byly nákladné na údržbu, obtížně škálovatelné a omezené v podpoře mobilní pracovní síly. Tradiční přístupy vyžadovaly samostatné systémy pro pevnou a mobilní komunikaci, což vedlo k roztříštěným uživatelským zážitkům, zdvojeným nákladům na infrastrukturu a složité režii správy.

Historický kontext vývoje Business Trunkingu zahrnuje rychlé přijetí mobilních zařízení v podnikovém prostředí a posun směrem ke cloudovým službám. Jelikož zaměstnanci stále více používali chytré telefony a tablety pro pracovní komunikaci, vznikla zjevná mezera mezi pokročilými funkcemi dostupnými na podnikových PBX systémech a základní funkcionalitou nabízenou standardními mobilními tarify. Business Trunking vznikl, aby tuto mezeru překlenul tím, že umožnil mobilním operátorům poskytovat služby ekvivalentní PBX přímo na mobilní zařízení, čímž pro mnoho podnikových uživatelů odpadla potřeba samostatné infrastruktury pro pevnou linku.

Business Trunking řeší několik klíčových problémů v podnikové komunikaci. Odstraňuje omezení předchozích přístupů tím, že poskytuje jednotné řešení kombinující výhody mobility buněčných sítí s pokročilými funkcemi podnikových telefonních systémů. To umožňuje podnikům efektivněji podporovat vzdálené pracovníky, snížit kapitálové výdaje na hardwarové PBX systémy a zjednodušit správu prostřednictvím centralizované administrace. Standardizovaný přístup definovaný 3GPP zajišťuje interoperabilitu mezi různými výrobci síťových zařízení a poskytovateli služeb, čímž předchází závislosti na jediném dodavateli a podporuje konkurenci na trhu podnikových komunikací.

## Klíčové vlastnosti

- Podpora podnikového číslovacího plánu s interním číslováním přípon
- Integrace a synchronizace s firemním adresářem
- Pokročilé funkce hovorů včetně přepojení, parkování a převzetí
- Směrování hovorů na základě času, cíle a uživatelských skupin
- Sjednocená komunikace přes pevné a mobilní koncové body
- Administrativní rozhraní pro správu uživatelů a funkcí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PBX – Private Branch eXchange](/mobilnisite/slovnik/pbx/)

## Definující specifikace

- **TS 22.519** (Rel-19) — NGN Business Communication Requirements

---

📖 **Anglický originál a plná specifikace:** [BT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bt/)
