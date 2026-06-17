---
slug: "cck"
url: "/mobilnisite/slovnik/cck/"
type: "slovnik"
title: "CCK – Corporate Control Key"
date: 2025-01-01
abbr: "CCK"
fullName: "Corporate Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cck/"
summary: "Bezpečnostní mechanismus zavedený ve specifikaci 3GPP Release 4 pro ověřování a autorizaci přístupu k podnikové síti prostřednictvím veřejných mobilních sítí. Umožňuje zabezpečenou podnikovou komunika"
---

CCK je bezpečnostní mechanismus, který poskytuje vyhrazený autentizační klíč oddělený od přihlašovacích údajů uživatele na SIM kartě, aby umožnil zabezpečený přístup k podnikové síti prostřednictvím veřejných mobilních sítí.

## Popis

Corporate Control Key (CCK) je komponenta bezpečnostní architektury definovaná ve specifikacích 3GPP, která vytváří rámec pro podnikem řízené ověřování a autorizaci při přístupu k podnikovým službám prostřednictvím veřejné pozemní mobilní sítě (PLMN). Funguje jako doplňkový bezpečnostní přístupový prostředek, odlišný od mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a autentizačních klíčů uložených na univerzálním modulu identity účastníka (USIM). CCK je zřízen a spravován podnikovou entitou, nikoli mobilním operátorem ([MNO](/mobilnisite/slovnik/mno/)), což podniku umožňuje udržovat přímou kontrolu nad tím, která zařízení a uživatelé mohou přistupovat k jeho privátním síťovým prostředkům přes PLMN.

Architektonicky mechanismus CCK zahrnuje několik klíčových komponent. Podniková síť hostuje funkci správy podnikového řídicího klíče (CCK-MF), která je zodpovědná za generování, distribuci a odvolávání CCK pro autorizované podnikové uživatele a jejich uživatelská zařízení (UE). UE musí být vybaveno USIM podporujícím CCK nebo samostatným bezpečnostním prvkem schopným uložit podnikový klíč. Během procedur připojení k síti nebo žádostí o službu zaměřených na podnikový přístup mohou UE a síť vyvolat proceduru autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) založenou na CCK. Tato procedura může probíhat paralelně s nebo jako alternativa ke standardní proceduře UMTS Authentication and Key Agreement (AKA), která používá přihlašovací údaje od MNO.

Technické fungování zahrnuje to, že UE předloží podnikovou identitu (např. Corporate Subscriber Identity) spolu s IMSI nebo místo něj. Visitor Location Register (VLR) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) obsluhující sítě rozpozná žádost o podnikový přístup a může směrovat autentizační signalizaci k podnikovému autentizačnímu serveru nebo síťové funkci pro propojení. CCK, známý pouze podnikové entitě a bezpečnostnímu prvku v UE, je použit ke generování autentizačních vektorů (dvojic výzva-odpověď a šifrovacích/integritních klíčů) specifických pro podnikovou relaci. Tím vzniká zabezpečený tunel nebo logicky oddělená komunikační cesta pro podniková data, s bezpečnostními klíči odvozenými nezávisle na klíčích MNO.

Jeho role v síti spočívá v usnadnění zabezpečeného přístupu k 'podnikovému virtuálnímu privátnímu síti' přes buněčnou infrastrukturu. Poskytuje základ pro služby jako přístup k mobilní intranetové síti, podnikový e-mail a zabezpečené hlasové hovory, kde podnik vyžaduje záruku, že přístup je povolen pouze jeho zaměstnancům s platnými přihlašovacími údaji vystavenými společností. Rámec CCK zajišťuje, že konečnou autoritou pro udělení přístupu k jeho prostředkům je podnik, nikoli MNO, i když data procházejí rádiovou a jádrovou sítí MNO. Toto oddělení kompetencí je klíčové pro podnikové bezpečnostní politiky a suverenitu nad daty.

## K čemu slouží

Corporate Control Key byl vytvořen, aby řešil rostoucí potřebu zabezpečeného, podnikem řízeného mobilního přístupu na počátku 21. století, kdy podniky začaly přijímat služby mobilních dat. Před jeho zavedením se podnikový přístup přes sítě GSM/[GPRS](/mobilnisite/slovnik/gprs/) typicky spoléhal na autentizaci účastníka od [MNO](/mobilnisite/slovnik/mno/) (prostřednictvím SIM) následovanou zabezpečením na aplikační vrstvě, jako jsou VPN. Tento model nedával podniku žádnou přímou kontrolu nad počáteční autentizací přístupu na síťové úrovni; důvěra byla zcela vložena do MNO, aby správně identifikovalo účastníka. Podniky, zejména ve finančnictví, státní správě a velkých korporacích, potřebovaly mechanismus k uplatnění vlastních politik ověřování a autorizace v okamžiku připojení k síti pro citlivou komunikaci.

CCK to vyřešil zavedením druhého, nezávislého autentizačního faktoru spravovaného podnikovou entitou. To umožnilo podnikům vydávat vlastní zabezpečené přihlašovací údaje (CCK) do zaměstnaneckých zařízení, což jim umožnilo přímo se ověřovat k podnikové síti přes PLMN. Řešil omezení, jako je neschopnost nezávisle na SIM od MNO odvolat přístup, absence podnikové identity v počátečním rádiovém spojení a snaha o end-to-end kontrolu zabezpečení od podniku až k zaměstnaneckému zařízení. Motivací bylo učinit z PLMN důvěryhodné rozšíření podnikové sítě tím, že se podnikové zabezpečení zabudovalo do standardizovaných procedur síťového přístupu, namísto toho, aby bylo považováno za nadstavbovou aplikaci.

Historicky byl CCK součástí rané práce 3GPP na vylepšení buněčných sítí pro potřeby podniků a vertikálních trhů a předcházel komplexnějším rámcům, jako je Network Slicing v 5G. Představoval základní krok k víceklientskému zabezpečení a konceptu oddělení 'předplatného' (vztah uživatele k MNO) od 'přihlašovacích údajů ke službě' (vztah uživatele k poskytovateli služeb). I když jeho rozšířené komerční nasazení bylo omezené, koncepty, které prosadil, ovlivnily pozdější vývoj ve federované autentizaci, SIM kartách s více přihlašovacími údaji a bezpečnostních architekturách pro privátní sítě a síťové řezy.

## Klíčové vlastnosti

- Umožňuje podnikem řízenou autentizaci nezávislou na přihlašovacích údajích na SIM kartě od MNO
- Podporuje samostatnou podnikovou identitu účastníka pro síťový přístup
- Umožňuje odvození podnikově specifických šifrovacích a integritních klíčů pro ochranu rádiového rozhraní
- Usnadňuje podnikovou kontrolu nad odvoláním přístupu a správou životního cyklu přihlašovacích údajů
- Poskytuje standardizovanou architekturu pro podnikovou autentizaci prostřednictvím funkce správy CCK
- Umožňuje zabezpečený přístup k podnikovým službám přes veřejné rádiové přístupové sítě

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [CCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/cck/)
