---
slug: "tliv"
url: "/mobilnisite/slovnik/tliv/"
type: "slovnik"
title: "TLIV – Type Length Instance Value"
date: 2025-01-01
abbr: "TLIV"
fullName: "Type Length Instance Value"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tliv/"
summary: "Základní kódovací formát používaný v protokolových zprávách 3GPP, zejména v GPRS Tunneling Protocol (GTP). Strukturuje informační prvky (IE) jako trojici TLV (Typ-Délka-Hodnota) s přidaným polem Insta"
---

TLIV je základní kódovací formát 3GPP, který strukturuje informační prvky protokolu jako čtveřici Typ-Délka-Instance-Hodnota, aby bylo možné rozlišit mezi více prvky stejného typu pro efektivní a jednoznačné parsování.

## Popis

Type Length Instance Value (TLIV) je datový kódovací formát, který rozšiřuje běžné schéma Typ-Délka-Hodnota ([TLV](/mobilnisite/slovnik/tlv/)) začleněním pole Instance. Je hojně používán v protokolech 3GPP, nejvýznamněji v informačních prvcích ([IE](/mobilnisite/slovnik/ie/)) [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) pro řídicí ([GTP-C](/mobilnisite/slovnik/gtp-c/)) i uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)). Každý IE zakódovaný ve formátu TLIV se skládá ze čtyř po sobě jdoucích polí. Pole Typ (1 nebo 2 oktety) identifikuje druh přenášené informace (např. [IMSI](/mobilnisite/slovnik/imsi/), QoS profil nebo [TEID](/mobilnisite/slovnik/teid/)). Pole Délka (2 oktety) určuje celkovou délku v oktetech následujících polí Instance a Hodnota. Klíčovým doplňkem je pole Instance (1 oktet), které slouží jako rozlišovač. To umožňuje zahrnout do jedné protokolové zprávy více IE stejného typu bez nejednoznačnosti. Například zpráva GTP-C může obsahovat několik IE Bearer Context (stejný Typ) pro různé přenašeče, přičemž každý je rozlišen jedinečnou hodnotou Instance. Nakonec pole Hodnota obsahuje vlastní datovou náplň, jejíž struktura je definována specifikací konkrétního IE. Formát TLIV poskytuje samopopisný a flexibilní rámec. Dekodéry protokolu mohou zprávy parsovat načtením pole Typ a v případě nerozpoznaného typu přeskočit data na základě hodnoty Délky (což zajišťuje zpětnou kompatibilitu) a správně přiřadit více instancí dat. Kódování je zarovnané na oktety a používá se pro povinné i volitelné IE. Jeho návrh je klíčový pro rozšiřitelnost signalizace v jádru sítě 3GPP, protože umožňuje přidávat nové IE v pozdějších vydáních bez narušení stávajících implementací, které mohou neznámé typy jednoduše ignorovat.

## K čemu slouží

Formát TLIV byl vytvořen, aby vyřešil potřebu robustního, rozšiřitelného a jednoznačného kódovacího schématu pro komplexní signalizaci protokolů v mobilních jádrových sítích. Jednoduché TLV kódování zvládne základní data, ale zprávy řídicí roviny často vyžadují více instancí stejného typu informace (např. více QoS profilů pro relaci). Bez pole Instance by rozlišení těchto opakujících se výskytů vyžadovalo složitá a neefektivní řešení. Struktura TLIV tento problém řeší tím, že poskytuje čistý, standardizovaný způsob balení a rozbalování vnořených nebo opakujících se informačních prvků. Jeho zavedení, zejména u GTP, poskytlo budoucně odolný základ pro rozhraní Evolved Packet Core (EPC) a 5G Core (5GC). Jak se služby vyvíjely od základního GPRS ke komplexnímu síťovému řezání a edge computingu v 5G, byly definovány stovky nových IE. Formát TLIV zajišťuje, že nové síťové funkce mohou zavádět nové typy IE a starší uzly je mohou bezpečně ignorovat použitím pole Délka pro přeskočení neznámých dat. Tato zpětná kompatibilita byla klíčová pro postupný, více-dodavatelský zavádění nových funkcí 3GPP v globálních sítích.

## Klíčové vlastnosti

- Čtyřpolní struktura: Typ, Délka, Instance, Hodnota
- Pole Instance umožňuje více IE stejného typu v jedné zprávě
- Samopopisný formát umožňuje zpětnou i dopřednou kompatibilitu
- Hojně používán v GTP-C a GTP-U pro rozhraní EPC a 5GC
- Pole Délka umožňuje parserům bezpečně přeskočit neznámé typy IE
- Standardizované kódování zarovnané na oktety pro spolehlivou interoperabilitu mezi různými dodavateli

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TLIV na 3GPP Explorer](https://3gpp-explorer.com/glossary/tliv/)
