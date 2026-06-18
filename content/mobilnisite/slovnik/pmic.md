---
slug: "pmic"
url: "/mobilnisite/slovnik/pmic/"
type: "slovnik"
title: "PMIC – Port Management Information Container"
date: 2025-01-01
abbr: "PMIC"
fullName: "Port Management Information Container"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pmic/"
summary: "Datová struktura používaná v rámci 5G Core Network pro přenos informací o správě portů, jako je stav a konfigurace portu, mezi síťovými funkcemi. Primárně se používá při interakci mezi funkcí správy r"
---

PMIC je datová struktura používaná v 5G Core Network pro přenos informací o správě portů mezi funkcí správy relací (SMF) a funkcí uživatelské roviny (UPF) za účelem správy kontextů relací N4.

## Popis

Port Management Information Container (PMIC) je protokolová datová jednotka definovaná v rámci protokolu Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)) používaného na rozhraní N4 mezi funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core. Jedná se o informační prvek ([IE](/mobilnisite/slovnik/ie/)) přenášený ve zprávách PFCP pro úpravu nebo zřízení relace. PMIC obsahuje podrobné informace o správě konkrétních portů přidružených k [PDU](/mobilnisite/slovnik/pdu/) relaci, což je zvláště relevantní pro scénáře zahrnující PDU relace typu Ethernet nebo jiné datové toky vyžadující explicitní řízení portů.

Z architektonického hlediska, když SMF potřebuje instruovat UPF ke správě portů pro připojení uživatelské roviny – například pro povolení, zakázání nebo konfiguraci parametrů na konkrétním Ethernet portu – zahrne PMIC do příslušné PFCP zprávy. Kontejner může specifikovat číslo portu, přidruženou [MAC](/mobilnisite/slovnik/mac/) adresu (pro Ethernet), administrativní stav (up/down) a další atributy specifické pro port. UPF po přijetí tuto konfiguraci aplikuje na své prostředky uživatelské roviny. To umožňuje detailní kontrolu nad prostředím pro přeposílání dat na UPF.

Jeho úlohou je umožnit 5G Core podporovat služby, které vyžadují explicitní správu na vrstvě 2, jako je konvergence pevných a mobilních sítí, průmyslový IoT s Ethernet backhaulem nebo síťové segmentování se specifickou izolací na úrovni portů. PMIC abstrahuje detaily správy portů do standardizovaného kontejneru, čímž zajišťuje interoperabilitu mezi SMF a UPF od různých dodavatelů. Funguje ve spojení s dalšími PFCP IE, které definují pravidla detekce paketů, akce pro přeposílání a vynucování QoS, aby plně orchestraval cestu uživatelské roviny.

## K čemu slouží

PMIC byl zaveden, aby řešil potřebu explicitní správy portů v rámci uživatelské roviny 5G Core, což je požadavek, který nabyl na významu s rozšířením 5G pro podporu ne-IP typů [PDU](/mobilnisite/slovnik/pdu/) relací, zejména Ethernetu. Předchozí architektury mobilního jádra byly primárně navrženy pro IP provoz ([GTP](/mobilnisite/slovnik/gtp/) tunely), kde byla správa portů implicitní nebo řešená na IP vrstvě. Podpora Ethernet PDU relací v 5G, poháněná případy užití jako průmyslová automatizace a konvergence pevných sítí, vyžadovala schopnost spravovat Ethernet switch porty v rámci UPF.

Problém, který řeší, je absence standardizovaného mechanismu pro konfiguraci a správu fyzických nebo logických portů na funkci uživatelské roviny (UPF) ze strany řídicí roviny (SMF). Bez PMIC by správa Ethernet portů vyžadovala proprietární rozšíření, což by bránilo interoperabilitě mezi více dodavateli a komplikovalo orchestraci služeb pro scénáře s pevným přístupem a podnikové scénáře.

K jeho vytvoření motivovala práce 3GPP na podpoře integrovaného přístupu a přenosu (IAB), konvergence pevných a bezdrátových sítí a síťového segmentování pro vertikální odvětví. Tyto vyžadují, aby 5G systém fungoval jako jednotná transportní síť schopná zpracovávat protokoly vrstvy 2 se stejnou úrovní programovatelnosti a řízení jako tradiční IP relace. PMIC poskytuje tento základní stavební blok pro správu na úrovni portů v rámci standardizovaného protokolu N4.

## Klíčové vlastnosti

- Standardizovaný informační prvek (IE) v rámci protokolu PFCP na rozhraní N4
- Přenáší instrukce pro správu portů z SMF do UPF
- Podporuje konfiguraci stavu portu (administrativně up/down) a parametrů
- Zásadní pro správu PDU relací typu Ethernet a přidružených MAC adres
- Umožňuje explicitní řízení portů uživatelské roviny pro služby jako konvergence pevných a mobilních sítí
- Usnadňuje interoperabilitu v nasazeních 5G Core s více dodavateli zahrnujících Ethernet uživatelskou rovinu

## Související pojmy

- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [PMIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmic/)
